import numpy as np

import logging
logger = logging.getLogger(__name__)

try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage

from PIL import ImageOps


class _Image:
    def __init__(self):
        self._image = None
        self._image_type = None 

        self.width = 0
        self.height = 0
        self.channels = 0

    def show(self, ax, **kwargs):
        ax.imshow(self._image, **kwargs)

    def save(self, name, **kwargs):
        im = PILImage.fromarray(np.uint8(self._image))
        im.save(name)

    @property
    def image(self):
        # frozen type
        return self._image

    @image.setter
    def image(self, image):
        if self._image_type and type(image) == self._image_type:
            self._image = image 
            
            self._update_shape()

        elif self._image_type == None:
            logger.debug("Setting image type to {}".format(type(image)))
            self._image_type = type(image)
            self._image = image

        else: 
            raise Exception("Bad image type: {}".format(type(image)))

    def _update_shape(self):
        # todo: update how this works
        shape = np.array(self.image).shape
        if len(shape) == 2:
            # greyscale 
            self.height, self.width = shape
        elif len(shape) == 3:
            self.height, self.width, self.channels = shape
        else:
            raise Exception("Invalid image shape: {}".format(shape))


    def expand(self, width, colour):
        self.image = ImageOps.expand(
                self.image, border=width, fill=colour
            )