# What happens when you import camera-scanned RAW negatives?

Auto Process is preselected during initial setup. Once you accept it, import a single RAW capture or a full roll of individually captured frames. NextFrame processes each frame automatically.

## What Auto Process does

1. **Crop and straighten.** NextFrame locates the frame, corrects its angle and keeps or trims the film border according to your crop preference.
2. **Find the exposure area.** It selects the picture area for exposure analysis, excluding the holder, sprocket holes and adjacent frames.
3. **Sample the film base (Dmin).** It looks for a clear, unexposed patch of film. The color and density of this patch provide a reference for inversion.
4. **Invert the negative.** It uses the base sample and exposure area to produce a positive and applies your chosen color mode.
5. **Fill the sprocket holes.** When you keep the film border, detected sprocket holes are filled white.
