# How to split a film strip scan into individual frames

When one FFF, TIFF, or DNG scan contains several exposures, NextFrame can create a cropped copy for each frame. Use automatic splitting on supported originals, or press F to crop the strip by hand. Export the copies to save each frame as its own image file.

## Flextight X5 and FFF workflow: choosing the original scan

For a Hasselblad Flextight X5 workflow, start with the original 3F scan. The worked example uses `1 002.tiff`, a TIFF with a Flextight input profile that NextFrame reads as Scan3F. Viewed horizontally, it contains two strips of six exposures each. Select the full scan to begin splitting.

![Original Flextight negative scan viewed horizontally with two rows of six exposures](../assets/media/flextight-strip.webp)

## Automatic FFF split

1. Import the scan and select the whole strip in the library.
2. For a supported original, choose “Process FFF/DNG automatically” from its context menu or click Auto split. For example, when working with a Hasselblad Flextight X5 strip, select the original FFF scan.
3. Under Film Format, choose half-frame, 135, 6×6, or 6×7.
4. Check the detected strip count and total frames, then confirm to create the cropped copies.
5. If you are asked to realign and rebalance color, choose what you need. Skip it when the color is already where you want it.
6. Check the edges, orientation, and color of each copy, then export.

Use a manual crop for XPAN and for scans that were not detected reliably. Automatic splitting creates separate editable copies. Those copies still have to be saved as image files through the export window.

**Check the frame boundaries.** The overlay below plots the 12 saved crop rectangles on the original scan, numbered in reading order. Look at the gap between 03 and 04. Each rectangle should end inside its own exposure. If a crop includes the neighboring exposure, open that copy, press `F`, adjust its edge, and confirm.

![Twelve numbered crop rectangles from the saved frame copies overlaid on the original scan](../assets/media/flextight-frame-map.webp)

**Check orientation and a single result.** This contact sheet uses the developed previews of all 12 copies from the same scan. Frames 01 and 02 are upright portraits and 03 is a landscape. Open 03 and check the horizon, driftwood, and left and right edges for any part of the next frame.

![Twelve developed previews in the same order as the numbered crop map](../assets/media/flextight-contact.webp)

![Developed preview of frame 03 with driftwood on the beach](../assets/media/flextight-frame-03.webp)

## Crop a strip by hand

1. After import, count the strips and the frames on each strip. Confirm orientation and format.
2. Press `A` and draw the useful area inside one strip. If you need a Dmin sample, press `Q` on clean base or in the gap between frames.
3. Press `F` to crop, and choose Strip.
4. Set the number of groups, frames per group, and spacing. Adjust the overall box, the offset between groups, and the angle.
5. Line up the first frame and the last frame, then check the frames in between. A crop box must not cross into the next picture.
6. Confirm the crop and check the result count in the filmstrip.

If frame count, spacing, or format is inconsistent inside one file, work in groups. Crop frame by frame when you have to.

## Inversion after the split

Select the split results. Hold `A` and choose Exposure Range 90% as a common starting point. That setting keeps 90% of the width and 90% of the height. Check each frame for interfering color. Sky, snow, and similar pictures can use their own range.

## Export

For this scan, select the 12 cropped copies and open export (`⌘ S` on macOS or `Ctrl S` on Windows). Check that the selection count is 12. For web sharing, choose JPEG, SDR, and sRGB, select the destination, and start the export. Check the output folder for 12 individual images and open frame 03 to compare it with the driftwood preview above. See [batch export settings](10-export.html).
