from BRImage.feeds.base_feed import BaseFeed

import PIL
import numpy as np

import logging

logger = logging.getLogger(__name__)


class GlitchImageFeed(BaseFeed):

    def __init__(self, gimage):
        super().__init__()
        self.gimage = gimage
    
    @property
    def width(self):
        return self.gimage.width
    
    @property
    def height(self):
        return self.gimage.height

    def _as_array(self, colourfmt):
        # override
        return np.array(self.gimage.image.convert(colourfmt))

    def _expand(self, width, colours):
        logger.debug("Expanding by margin: {}".format(width))
        try:
            self.gimage.expand(100, colours)
        except TypeError:
            self.gimage.expand(100, "white")

    def apply(self, new_image):
        self.gimage.image = PIL.Image.fromarray(new_image)
        