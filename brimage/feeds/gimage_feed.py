import logging

import PIL
import numpy as np

from brimage.feeds.base_feed import BaseFeed


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

    def as_array(self, colourfmt):
        # override
        return np.array(self.gimage.image.convert(colourfmt))

    def expand(self, width, colours):
        #  deprecated: will be removed
        try:
            self.gimage.expand(width, colours)
        except TypeError:
            self.gimage.expand(width, "white")

    def apply(self, new_image):
        self.gimage.image = PIL.Image.fromarray(new_image)
