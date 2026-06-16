import WebSocket from "ws";
import { randomUUID } from "crypto";
import { writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT_DIR = join(__dirname, "../assets/imgs");
const CHANNEL = "g8nm1obm";
const PORT = 3055;

const EXPORTS = [
  { nodeId: "1662:1447", file: "feature-negative.png" },
  { nodeId: "1662:1448", file: "feature-positive.png" },
  { nodeId: "1662:1456", file: "feature-border-no-margin.png" },
  { nodeId: "1663:1458", file: "feature-border-with-margin.png" },
  { nodeId: "1661:1422", file: "feature-exif-hdr.png" },
];

const pending = new Map();
let channel = null;

function send(ws, payload) {
  ws.send(JSON.stringify(payload));
}

function command(ws, cmd, params = {}, timeoutMs = 120000) {
  return new Promise((resolve, reject) => {
    const id = randomUUID();
    const timer = setTimeout(() => {
      pending.delete(id);
      reject(new Error(`Timeout: ${cmd}`));
    }, timeoutMs);

    pending.set(id, {
      resolve: (v) => {
        clearTimeout(timer);
        resolve(v);
      },
      reject: (e) => {
        clearTimeout(timer);
        reject(e);
      },
    });

    if (cmd === "join") {
      send(ws, {
        id,
        type: "join",
        channel: params.channel,
        message: { id, command: "join", params: { ...params, commandId: id } },
      });
      return;
    }

    send(ws, {
      id,
      type: "message",
      channel,
      message: {
        id,
        command: cmd,
        params: { ...params, commandId: id },
      },
    });
  });
}

async function exportAll() {
  mkdirSync(OUT_DIR, { recursive: true });

  await new Promise((resolve, reject) => {
    const ws = new WebSocket(`ws://localhost:${PORT}`);

    ws.on("open", async () => {
      try {
        await command(ws, "join", { channel: CHANNEL });
        channel = CHANNEL;
        console.log("Joined channel:", CHANNEL);

        for (const item of EXPORTS) {
          console.log("Exporting", item.file, "...");
          const result = await command(ws, "export_node_as_image", {
            nodeId: item.nodeId,
            format: "PNG",
            scale: 2,
          });
          const data = result.imageData;
          if (!data) throw new Error(`No image data for ${item.file}`);
          writeFileSync(join(OUT_DIR, item.file), Buffer.from(data, "base64"));
          console.log("Saved", item.file);
        }

        ws.close();
        resolve();
      } catch (err) {
        ws.close();
        reject(err);
      }
    });

    ws.on("message", (raw) => {
      try {
        const json = JSON.parse(raw.toString());
        const msg = json.message ?? json;
        if (msg?.id && pending.has(msg.id)) {
          if (msg.error) pending.get(msg.id).reject(new Error(msg.error));
          else pending.get(msg.id).resolve(msg.result);
          pending.delete(msg.id);
        }
      } catch (e) {
        console.error("Parse error:", e);
      }
    });

    ws.on("error", reject);
  });
}

exportAll()
  .then(() => console.log("Done"))
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });
