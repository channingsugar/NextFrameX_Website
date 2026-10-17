# Absolute masks on a strip

Absolute masks invert and adjust each frame on the same strip scan, then split the strip once at the end.

## Add masks

1. Set a first exposure range for the whole strip, and sample Dmin if you need it.
2. In the mask panel, add a Rectangle and choose Absolute.
3. Place the rectangle on one frame. Make a mask for each other frame. Keep the size the same when the format is the same.
4. Move them so the masks do not overlap. For the first setup, use no feather and do not invert the mask.

## Adjust each frame

Select the mask you want to change, then edit inversion, exposure, and color. To share a range step, select several masks and choose Exposure Range 90%, then check each frame.

An absolute mask can invert on its own. A relative mask adjusts a local area on top of the image you already have. Watch whether the right-hand panel is acting on the mask or on the whole photo.

## Crop and export

Press `F` for the strip crop, line every crop box up with a frame, confirm, and check each copy. Color and sample range should match before and after the split. When they do, select the results and open export.

Crop boxes are covered in [Strip scans](04-strip.html). Color is covered in [Color](08-color.html).
