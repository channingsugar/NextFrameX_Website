# Density inversion and sampling

The inversion panel controls a negative’s brightness and color through a density-domain conversion and the DCMY settings. Exposure range, Dmin, and Dmax set the analysis area and the reference points.

For the optical density equation and a real camera-scan example, see [the color science of film negative conversion](16-density-color-science.html).

## Density-domain inversion

Film density and transmitted light are related logarithmically. Density-domain inversion works in that relationship, then uses channel baseline, gain, and tone to produce a positive. The controls are not the same as a simple RGB invert.

Press `C` to toggle inversion. Press `S` for automatic alignment. Manual DCMY adjustments are in [Film Color Grading](08-color.html).

## Exposure range

The exposure range decides which areas are analyzed. It does not change the export boundary.

- Press `A`, then drag on the picture to draw the analysis area.
- Hold `A` to choose a preset ratio, or choose Auto to process again.
- Press `V` to show or hide the range marks.

Keep the exposure range inside the picture, clear of the film holder, sprocket holes, neighboring frames, and large areas of distracting color.

If the range looks right but the positive still has a color cast, check two things.

1. **Are there bright colors inside the range?** A few brightly colored lights can influence the analysis even in an otherwise neutral scene. Look for vivid red or yellow lights, especially where a highlight is complementary in color to its surroundings. Redraw the range to leave those lights outside it, then compare the positives to see whether the cast is weaker.
2. **Is the scene nearly a single color?** A sky, clouds, or a snow-covered mountain may offer no reliable black point. Try including a small patch of clean film base in the exposure range, then compare the result.

![Exposure range and sample marks on a raw-folder photo](../assets/media/range.webp)

Press `V` to show the exposure range and sample marks. The picture above is from the current Develop workspace: the range sits inside the picture and avoids sprocket holes and edge codes.

## Dmin

Press `Q` for Dmin and click clean film base. The narrow black edge around the frame, and the gap between frames, are usually usable. Avoid printed codes, holes, and the scanner bed.

If there is no clear base, try the darkest reliable area in the inverted positive. That means a dark area in the positive, not the darkest part of the negative original. Compare color, fog, and contrast after sampling. If it gets worse, click Clear next to Dmin, or undo.

Dmin can be left unset. You do not have to find a sample on every photo.

## Dmax

Hold `Q` and choose Dmax. Sample the brightest neutral highlight in the positive that has not clipped, such as a white wall, white clothing, or a white cloud. Avoid colored lights and colored reflections.

Try Dmax after range, white balance, and cast strength have not improved the picture.

## Sample position and crop

A sample can sit outside the final crop, but it should be the same piece of film under the same light. Sample first, then crop away the outer area you do not want. Even when you keep the base, remove the continuous white border outside the film.
