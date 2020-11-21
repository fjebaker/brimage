from BRImage.glitchcore.image import _Image
import PIL
import numpy as np

import logging
logger = logging.getLogger(__name__)


class OverlayBase(_Image):
    def __init__(self, gimage, rinit=255, ginit=255, binit=255):
        super().__init__()
        self._gimage = gimage
        self._init_colours = (rinit, ginit, binit)

        self._make_canvas()

    def _make_canvas(self):
        self.image = np.array(PIL.Image.new(
            "RGB", [self._gimage.width, self._gimage.height], self._init_colours
        ))

    def _image_to_pil_image(self):
        return PIL.Image.fromarray(self.image)

    def _get_gimage_data(self, colourfmt="L"):
        """ Returns np array of the original GlitchImage in the given colour format """
        return np.array(self._gimage.image.convert(colourfmt))
    
    def _get_data(self):
        """ Returns np array of the image data """
        return self.image

    def _expand(self, width):
        logger.debug("Expanding by margin: {}".format(width))
        try:
            self._gimage.expand(100, self._init_colours)
        except TypeError:
            self._gimage.expand(100, "white")

    def apply(self):
        self._gimage._image = self._image_to_pil_image()
