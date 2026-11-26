# How to remove dust from infrared and RGB film scans

Check whether the scan includes an infrared channel. NextFrame can use that channel to locate and repair dust. For camera scans and RGB-only files, use on-device AI detection across the frame or in a selected area. For a single speck, use the manual brush.

For scattered dust in an RGB image, start with [automatic dust removal](#automatic-dust-removal). For an infrared scan or dust confined to one area, go to [infrared and local AI cleaning](#infrared-and-local-ai-cleaning).

## Sprocket fill and borders

1. Crop with Keep Base so the edge codes and sprocket holes you want remain.
2. Press `G` to turn on sprocket fill, and hold `G` to adjust the threshold.
3. Zoom in and check missed holes, edge codes, and dark parts of the picture. Lower the threshold if it fills areas it should not.
4. Crop away the continuous white border outside the base.

Sprocket fill is white. For a motion piece with a border, choose the Border template in Live export. See [Export](10-export.html).

## Automatic dust removal

1. Press `E` to open dust removal and choose Auto.
2. RGB detection uses a local model. If the panel prompts you to download or update it, complete that step before starting detection.
3. Click Detect dust and inspect the detected spots. Use Markers to show or hide their locations.
4. Adjust sensitivity, or edit the dust mask with the brush and eraser. If real texture was selected, lower the sensitivity or erase that area.
5. Click Remove and inspect the spot and the surrounding texture in the preview.
6. Press `Enter` to apply, or `Esc` to cancel.

If this computer does not support automatic dust removal, use the Manual page. Scroll to change the brush size, then click or drag to repair dust. Hold Space and drag to pan. `⌘ Z` undoes.

## Infrared and local AI cleaning

**For scans with an infrared channel.** Press `E` and choose Auto. Under Infrared Dust Removal, enable Markers to see which spots the scanner channel identifies, then enable Remove to inspect the repair. Watch nearby outlines and fine lines as you adjust infrared sensitivity. This method needs no AI model. The brush and eraser edit a separate mask and leave the infrared layer intact.

**For dust in one part of an RGB image.** If there are specks in one corner of a sky, choose Select on the Auto tab and drag a rectangle around them. Detection starts in that region. Inspect the markers, then click Remove. For a single isolated spot you can also use the brush on the Manual tab.

**How do I check that film detail survived?** Compare the same area at 100%. Check both the speck and the grain, hair, or branches beside it. If real texture is marked, lower the sensitivity for the detection method you are using and inspect the markers again.

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

## Simulated film borders {#simulated-film-base}

If a Hasselblad FFF scan was cropped to the image area, select its frames in the photo list and choose **Simulated Film Base…** from the context menu. Pick the film stock and format, check the starting frame number, then choose **Apply**. When you select several photos, frame numbering follows their order in the list.
