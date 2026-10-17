# Strip scans and frame splitting

Use this when one TIFF, FFF, or DNG contains several frames in a row.

## Automatic FFF split

1. Import the scan and select the whole strip in the library.
2. For material that supports automatic splitting, click Auto Split, or open the command from the photo’s context menu.
3. Under Film Format, choose half-frame, 135, 6×6, or 6×7.
4. Check the detected strip count and total frames, then confirm to create the cropped copies.
5. If you are asked to realign and rebalance color, choose what you need. Skip it when the color is already where you want it.
6. Check the edges, orientation, and color of each copy, then export.

Use a manual crop for XPAN and for scans that were not detected reliably. Automatic splitting creates separate editable copies. Those copies still have to be saved as image files through the export window.

![Frames after splitting folder 4879](../assets/media/strip.webp)

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

Select every split result you want to save and press `⌘ S`. If the strip has 12 frames, the export window should have those 12 results selected. After export, check the number of files on disk.
