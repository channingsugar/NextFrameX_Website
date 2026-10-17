# Connecting an agent

NextFrame exposes image tools to clients that speak local MCP. Once connected, you can name a folder, a processing path, and the changes you want in conversation.

## Set up the connection

1. Open NextFrame and go to Settings → Agent MCP….
2. Add the folders the agent is allowed to process, then click Enable Local MCP.
3. Copy the Codex or Cursor configuration shown in the window into that client’s MCP configuration.
4. Reload the client’s tools and have the agent check that NextFrame is connected.

Use the path shown in the window on this computer. After the app quits, enable the connection again. NextFrame does not need a large-model API key.

## Process a folder

You can tell the agent:

> Use NextFrame to process the folder "actual/path/to/files". Keep the film base for RAW frames, and remove it for strip scans. Check the crop and color of every frame, and show the results first.

Replace the path inside the quotes. To keep editing, name the file and the change, for example “Make _200885.ARW a little brighter, and keep the current color.”

For a photo you have already adjusted by hand, say that the current settings should stay, and that the change starts from the current look.

## Network

Leave cloud color correction on when the network supports it. If the color service cannot connect, say “Turn off cloud color correction for this run and continue locally.” An agent client being online does not mean NextFrame’s color service can connect.

## Check and export

Look at the preview. Check crop, range, sprockets, and color. Describe the next change if you need one.

The current MCP export command opens NextFrame’s export window. You choose the format and folder and finish the export. Afterward, check the actual files in the destination.
