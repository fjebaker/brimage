from BRImage.glitchcore.image import _Image
import PIL

from PIL import ImageOps


class OverlayBase(_Image):
    def __init__(self, gimage, rinit=255, ginit=255, binit=255):
        self._gimage = gimage

        self._init_colours = (rinit, ginit, binit)

        self.width, self.height = gimage.width, gimage.height
        self._image = PIL.Image.new(
            "RGB", [gimage.width, gimage.height], (rinit, ginit, binit)
        )

    def _image_to_pil_image(self):
        self._image = PIL.Image.fromarray(self._image)

    def expand(self, width):
        try:
            self._gimage._image = ImageOps.expand(
                self._gimage._image, border=width, fill=self._init_colours
            )
            self._image = ImageOps.expand(
                self._image, border=width, fill=self._init_colours
            )
        except TypeError:
            # botch fix for greyscale case
            self._gimage._image = ImageOps.expand(
                self._gimage._image, border=width, fill="white"
            )
            self._image = ImageOps.expand(self._image, border=width, fill="white")

    def apply(self):
        if not isinstance(self._image, PIL.Image.Image):
            self._image_to_pil_image()
        self._gimage._image = self._image
