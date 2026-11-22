# How to automatically convert a full roll of RAW film negatives without Lightroom

Turn on Auto Process in NextFrame and import a folder of camera-scanned RAW negatives. NextFrame detects, crops, inverts, and color-corrects each exposure using your preset. Review representative frames, adjust any exceptions, and batch export the positives in the same desktop app.

If one file contains a row of frames, start with [splitting a film strip scan](04-strip.html).

## From a roll of negatives to individual positives

Put the camera captures from one roll in one folder, with one exposure per RAW file. Set the processing preferences below, then import the folder into the library. Once processing finishes, review a typical frame, a dark one, and a bright one. Press `V` to check the base sample and exposure range. Press `A` to redraw a range that includes the next exposure. Select the frames you want, check their count in the export window, and export them together.

![The same camera-scanned frame in its embedded RAW preview on the left and its saved NextFrame positive preview on the right](../assets/media/raw-film-base-pair.webp)

Both views come from the same Sony α7R III capture. Use the tree trunk and sprocket holes to match the two images. Check that the analysis rectangle excludes adjacent exposures before judging detail in grass and shade. See [the color science of film negative conversion](16-density-color-science.html) for how the base sample affects color.

## Set the default

1. Open Settings → Processing Preferences, or press `⌘ Shift ,`.
2. Turn on Auto Process. Under Auto Crop, choose Keep Base or Remove Base. Choose Straighten if you only need the angle corrected.
3. Set automatic Dmin, automatic straightening, sprocket fill, automatic tone, and temperature and tint as needed.
4. Choose the default color mode. Turn on cloud color-cast correction if you want it, and keep a network connection available.
5. Import the RAW files and wait until processing finishes.

Processing preferences apply to newly imported photos and to photos after a reset. They do not rewrite an edit that is already open. Strip scans do not use the single-RAW automatic path.

## Run it again

In Develop, select the photo, hold `A` to open the dial, and choose Auto. This recalculates inversion and related settings. To keep the hand adjustments you already made, press `⌘ D` first and work on a virtual copy.

Hold `D` to choose the automatic crop: keep the base, remove the base, or straighten. A short press of `D` toggles between the automatic crop and no crop. Hold `S` to choose Vivid, Natural, or Original tone.

## Check the crop and the range

Press `F` to crop. Check that the light panel, film holder, or a neighboring frame is not left in the edges. Drag an edge to change it, press `Enter` to confirm, or `Esc` to discard this change.

Press `V` to show the marks. Check that the sample point sits on clean, unexposed film base and that the exposure rectangle covers the picture. If the rectangle includes sprocket holes, the holder, or the next frame, press `A` to redraw it. Hold `A` to pick a range preset.

![Saved analysis area in cyan and automatic Dmin sample in yellow, plotted on the same camera-scanned negative](../assets/media/raw-sampling-map.webp)

Here the cyan rectangle excludes the next frame, while the yellow circle lies close to the edge lettering. Try sampling a clear patch away from the letters and compare the whole positive. If there is no clear base, try the darkest reliable area in the positive. If the sample does not help, clear it. See [Inversion and sampling](07-inversion.html).

## Check the sprockets

With the base kept, press `G` to toggle sprocket fill, and hold `G` to adjust the threshold. Zoom in and look for holes that were missed. Also confirm that dark parts of the picture and the edge codes were not filled white. The final crop should not keep the continuous white border outside the film.

## Color and export

If the automatic result looks right, export it. If the whole frame has a cast, check the exposure range and film-base sample first. If neutral objects still look tinted, try the DCMY eyedropper, then fine-tune white balance as needed. See [Color](08-color.html). Press `⌘ S` to open export (`Ctrl S` on Windows).
