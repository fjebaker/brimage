from BRImage.glitchcore.image import _Image
import abc

import PIL 
import numpy as np

import logging

logger = logging.getLogger(__name__)


class BaseOverlay(_Image, abc.ABC):
    def __init__(self, feed, rinit=255, ginit=255, binit=255):
        super().__init__()
        self._feed = feed

        self.width = feed.width
        self.height = feed.height

        self._init_colours = (rinit, ginit, binit)

    def _make_canvas(self):
        image = [value * np.ones((self._feed.height, self._feed.width), dtype=np.uint8) for value in self._init_colours]
        image = np.stack(image, axis=-1)
        logger.debug(f"Canvas created with shape {image.shape}")
        self.image = image

    def _get_gimage_data(self, colourfmt="L"):
        """ Returns np array of the original GlitchImage in the given colour format """
        return self._feed._as_array(colourfmt)
        # np.array(self._gimage.image.convert(colourfmt))

    def _get_data(self):
        """ Returns np array of the image data """
        return self.image

    def _expand(self, width):
        self._feed._expand(width, self._init_colours)

    def apply(self):
        """ Propage the distorted image back up to the feed """
        self._feed.apply(self.image)

