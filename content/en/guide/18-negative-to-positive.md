# How a film negative becomes a positive

These two views show the same color negative photographed with a Sony α7R III. On the left is the preview embedded in the RAW file. On the right is the developed frame in NextFrame. Follow the tree trunk and the row of sprocket holes to match the two.

![The orange-masked negative on the left and the same frame of trees and grass as a positive on the right](../assets/media/raw-film-base-pair.webp)

## Import the negative

Import the camera RAW into NextFrame. With the automatic processing option selected during first-time setup, NextFrame finds and straightens the frame, determines the exposure range and inverts the negative on import. Open Develop to view the positive. You can also import a whole roll of individual captures together. [What happens automatically on RAW import](03-raw.html)

## Find the two references on the frame

![The film-base sample point and exposure analysis rectangle from the edit of this negative](../assets/media/raw-sampling-map.webp)

Press `V` to show the markers. **Find the film-base point first.** The unexposed film between the sprocket holes along the top edge is a useful Dmin reference. If the point lands inside a hole or on lettering, press `Q` and sample clean film base. **Then check the exposure rectangle.** It should cover the image in this frame. If it includes the holder or the next frame, press `A` and redraw it. This rectangle tells NextFrame where to analyze brightness. Press `F` to inspect the output crop separately. [Film-base sampling and exposure range](07-inversion.html)

## Read the positive

Look for detail in the shaded trees and separation in the highlights. The grass is green to begin with, so judge a color cast using a known neutral surface elsewhere in the scene. If you are happy with the result, export the frame. If a gray wall or a white shirt still looks blue or green, see [how to remove a color cast](17-remove-color-cast.html). For the reason behind the film-base sample, see [the color science of negative conversion](16-density-color-science.html).
