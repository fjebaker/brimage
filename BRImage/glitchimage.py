from BRImage.glitchcore.image import _Image
from BRImage.overlays import FreqModOverlay, RandomWalkOverlay

import logging
logger = logging.getLogger(__name__)


try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage


class GlitchImage(_Image):
    def __init__(self, path=None, data=None):
        """ Construct a GlitchImage from either an image path, or a data frame """
        super().__init__()

        if path and data:
            raise Exception("Cannot create a GlitchImage instance from both path and data. Please use only one kwarg.")
        elif path:
            self._load_from_path(path)
        elif data:
            self._load_from_data(data)
        else:
            raise Exception("No valid path or data arguments provided.")
            
        
    def _load_from_data(self, data):
        self._path = ":memory:"
        self.image = PILImage.fromarray(np.uin8(data))
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
