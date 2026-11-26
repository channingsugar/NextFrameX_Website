# How to remove a color cast from scanned film negatives

After inversion, find something that should look neutral in the scene: a gray wall, a white shirt or a gray card. Check it in the shadows and in the light. A cast across the whole frame calls for a different adjustment from a blue shadow under an otherwise white dress. Use the tool that fits what you see and stop when the frame looks right.

![The same street portrait before and after correction. The blue cast in the white clothing and pavement on the left is reduced on the right.](../assets/media/cast-street-pair.webp)

Compare the clothing and pavement on the left with the same areas on the right. Both lose their blue tint while the trees stay green. A white shirt at sunset, on the other hand, might look right with some warmth. Before adjusting color, press `V` to check the film-base point and exposure range. If a sprocket hole, edge marking or adjacent frame was sampled, [fix the inversion references first](07-inversion.html#dmin).

## Start with the DCMY eyedropper if you have a neutral reference

Hold `W`, choose the **DCMY eyedropper**, and click an evenly lit neutral patch in the positive preview. In this picture, try a patch of white fabric that still shows texture. Avoid glare and folds catching green light from the trees. NextFrame uses the sample to adjust the inversion. Check another neutral surface and the skin tones. If either shifts the wrong way, undo and sample a different spot. [Eyedropper shortcuts](11-shortcuts.html)

## Drag a DCMY waveform when the cast changes with brightness

Suppose the white shirt looks right but the shadow on a gray wall looks green. In the inversion panel, move the left end of **M**, the green channel, a little at a time. Watch the wall and check that the white shirt stays neutral. The left end changes the shadow baseline. The right end changes gain, which is easier to judge in brighter areas. C, M and Y correspond to red, green and blue; D adjusts overall brightness. [Waveform endpoints and channels](08-color.html#drag-the-dcmy-waveforms)

## Use the white-balance eyedropper for an overall warm or cool cast

Press `W` for the white-balance eyedropper, or hold `W` and select it by name. Sample a gray card, gray wall or textured white fabric in the same light as your subject. This adjusts temperature and tint. Check a second neutral surface under that light. When cool shade and warm sunlight share the frame, choose the light falling on your subject. [White-balance controls](08-color.html#white-balance-and-cast-strength)

## Adjust white balance by tonal range for mixed casts

If white clothing looks right but its shadows look blue, open **Shadows** in the white-balance panel and warm the temperature slightly. If only the midtones look green, open **Midtones** and move tint a little toward magenta. Check skin after each adjustment. **Highlights** and **Overall** are also available. The ranges select pixels by brightness. [White balance and the shortcut dial](15-controls.html#hold-a-key-to-open-the-dial)

## Compare the automatic color-cast model with P

Press `P` to toggle correction on the same frame. The model estimates a midtone correction for each RGB channel. **Color Cast Strength** controls how much of that correction is applied. Compare the shirt, pavement and skin with it on and off. If the shirt improves but skin becomes too cool, leave correction on and adjust its strength with the semicolon and apostrophe keys. A fresh cloud prediction requires a connection. [Automatic correction and strength](08-color.html#white-balance-and-cast-strength)

## Use manual levels for a remaining cast in one channel

Open **Levels** and select R, G or B. If the blacks and whites look right but mid-gray still looks blue, move the midpoint of the B channel slightly and watch the gray surface. For a cast confined to the darkest or brightest tones, inspect that channel’s input black or white point. Keep detail in dark hair and bright fabric. The master channel adjusts overall tone. Manual levels give you individual channel endpoints and midpoints; the P strength control scales the model’s correction. [Manual levels and correction strength](08-color.html#print-scan-luts-and-manual-levels)
