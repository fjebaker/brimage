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

    def map_algorithm(self, *args, **kwargs):
        """ To override: invocation function """
        return self.image

    def _make_canvas(self):
        image = [
            value * np.ones((self._feed.height, self._feed.width), dtype=np.uint8)
            for value in self._init_colours
        ]
        image = np.stack(image, axis=-1)
        logger.debug(f"Canvas created with shape {image.shape}")
        self.image = image

    def _get_from_feed(self, colourfmt="L"):
        """ Returns np array of the original GlitchImage in the given colour format """
        return self._feed._as_array(colourfmt)
        # np.array(self._gimage.image.convert(colourfmt))

    def _get_data(self):
        """ Returns np array of the image data """
        return self.image

    def _expand(self, width):
        logger.debug("Expanding by margin: {}".format(width))
        self._feed._expand(width, self._init_colours)

    def _reduce(self, width):
        logger.debug("Reducing by margin: {}".format(width))
        out_image = []
        for i in range(self.image.shape[-1]):
            channel = self.image[:, :, i]
            channel = channel[width:-width, width:-width]
            out_image.append(channel)
        self.image = np.stack(out_image, axis=-1)

    def _to_rgb(self):
        if len(self.image.shape) == 2:
            logger.debug("Cast to RGB from greyscale.")
            return np.stack([self.image.copy() for i in range(3)], axis=-1)
        else:
            logger.warning("Cast to RGB ignored, as image is three dimensional.")
            return self.image.copy()

    def apply(self):
        """ Propage the distorted image back up to the feed """
        self._feed.apply(self.image)
