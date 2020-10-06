from BRImage.glitchcore.image import _Image
import PIL


class OverlayBase(_Image):
    def __init__(self, gimage, rinit=255, ginit=255, binit=255):
        self._gimage = gimage

        self.width, self.height = gimage.width, gimage.height
        self._image = PIL.Image.new(
            'RGB', 
            [gimage.width, gimage.height], 
            (rinit, ginit, binit)
        )
