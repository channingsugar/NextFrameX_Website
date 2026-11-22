# The color science of film negative conversion

A film scanner or camera measures light passing through a negative. Optical density expresses how strongly the film attenuates that light. In NextFrame, the film base and exposure range provide references for converting those measurements into a positive. You can then adjust tone and color separately.

## From transmitted light to density

Transmittance, T, is the fraction of incident light that passes through the film. Optical density is D = −log₁₀(T). A patch transmitting 10% of the light has density 1.0. At 1% it has density 2.0. A tenfold change in transmitted light is one step on this scale. This is a physical relationship for linear light measurements. An RGB number from a display JPEG already includes tone encoding.

For a worked introduction to transmittance and density, see Kodak’s *Basic Photographic Sensitometry Workbook*.

## Read the film base before judging color

An unexposed, developed margin on a color negative still has density and often looks orange. It transmits different amounts of red, green, and blue light. Sampling clean base gives the conversion a reference for those channel differences. A sprocket hole lets light through without passing through film. A printed edge code adds density of its own.

![The same Sony RAW frame in camera-preview and developed views, with sprocket holes and edge markings](../assets/media/raw-film-base-pair.webp)

In this camera scan, follow the top edge. There is film between the holes and around the lettering. Press `V` to check where the Dmin point landed. If it falls in a hole or on a letter, use `Q` to sample a clear patch of base. Keep the exposure rectangle inside the photograph. Press `A` if it needs redrawing. See [inversion and sampling](07-inversion.html) for Dmax and difficult frames.

## Separate exposure from a color cast

The D control adjusts the overall density baseline and gain. C, M, and Y affect the red, green, and blue channels respectively. The left end of each waveform controls its baseline and the right end its gain. A gray shadow that looks green and a white highlight that looks green can need different adjustments.

Start with the automatically converted frame. If a subject you know to be neutral has a cast, first check the sample and analysis area. Try the DCMY eyedropper on that neutral subject and inspect both shadows and highlights. Fine-tune white balance if necessary. The grass in the example is a poor neutral reference. For the controls, see [color adjustments](08-color.html).

## What can this example tell you about accuracy?

The pair shows how one real frame was interpreted. To measure color accuracy, photograph a reference target under documented lighting, keep capture and export settings consistent, and compare the converted patches with the reference values in the same color space. For an ordinary roll, compare skin, neutral objects and shadow detail across nearby frames while preserving the color of the original light.

To use this workflow on your own roll, follow [automatic RAW negative conversion](03-raw.html).
