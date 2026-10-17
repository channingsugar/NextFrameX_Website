# Sprockets, dust, and texture

Sprocket handling when you keep the film base, plus dust removal, sharpening, glow, and grain.

## Sprocket fill and borders

1. Crop with Keep Base so the edge codes and sprocket holes you want remain.
2. Press `G` to turn on sprocket fill, and hold `G` to adjust the threshold.
3. Zoom in and check missed holes, edge codes, and dark parts of the picture. Lower the threshold if it fills areas it should not.
4. Crop away the continuous white border outside the base.

Sprocket fill is white. For a motion piece with a border, choose the Border template in Live export. See [Export](10-export.html).

## Automatic dust removal

1. Press `E` to open dust removal and choose Auto.
2. The first time, download the dust-detection model when asked. After that, detection runs on this computer.
3. Click Detect Dust, turn on Show Dust, and look at the marked area.
4. Adjust sensitivity, or edit the dust mask with the brush and eraser. If real texture was selected, lower the sensitivity or erase that area.
5. Click Remove Dust, and use Compare to check the repair.
6. Press `Enter` to apply, or `Esc` to cancel.

If this computer does not support automatic dust removal, use the Manual page. Scroll to change the brush size, then click or drag to repair dust. Hold Space and drag to pan. `⌘ Z` undoes.

## Noise reduction and sharpening

Open Detail and adjust noise reduction and sharpening near 100% view. Look at sky, skin, edges, and fine texture. Too much sharpening makes bright edges. Too much noise reduction removes grain and detail.

## Glow

Open Glow and adjust strength, range, distance, and warmth. Watch the spread around highlights and the local contrast. Use the reset button on the right of the panel to return to the default.

## Grain

Under Glow, open Grain and adjust:

| Setting | Effect |
| --- | --- |
| Amount | Texture strength. 0 turns it off |
| Size | How large the grain looks |
| Roughness | The balance of fine texture and larger clumps |

Start with a low amount. At 100% view, look at skin, sky, and shadows, then adjust size and roughness. A scan that already has clear film grain does not need more.

## Apply to a batch

Copy settings from a reference photo. On the target, open the paste panel and check only the modules you want to sync. After a batch apply, check photos with different exposure and different subjects.
