from BRImage.glitchcore.image import _Image
from BRImage.overlays import FreqModOverlay, RandomWalkOverlay

import numpy as np

import logging
logger = logging.getLogger(__name__)


try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage


class GlitchImage(_Image):
    def __init__(self, *args):
        """ Construct a GlitchImage from either an image path, or a data frame """
        super().__init__()

        if len(args) > 1:
            raise Exception("Too many arguments provided.")
        else:
            arg = args[0]
            if type(arg) == str: 
                logger.debug("GlitchImage from path {}".format(arg))
                self._load_from_path(arg)
            elif type(arg) == np.ndarray:
                logger.debug("GlitchImage from data with shape {}".format(arg.shape))
                self._load_from_data(arg)
            else:
                raise Exception("Argument must be type string or ndarray.")
        
        logger.info(f"GlitchImage@{id(self)}: width: {self.width}, height: {self.height}")
        
    def _load_from_data(self, data):
        self._path = ":memory:"
        self.image = PILImage.fromarray(np.uint8(data))
        self.width, self.height = self.image.size
    
    def _load_from_path(self, path):
        self._path = path
        self.image = PILImage.open(path).convert("RGB")
        self.width, self.height = self.image.size

    def __str__(self):
        return "{}x{} GImage".format(self.width, self.height)

    def freqmod_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        return FreqModOverlay(self, **kwargs)

    def random_walk_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        return RandomWalkOverlay(self, **kwargs)
