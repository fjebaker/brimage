import logging

from PIL import Image as PILImage
import numpy as np

from brimage.glitchcore.image import _Image
from brimage.feeds import GlitchImageFeed

from brimage.overlays import FreqModOverlay, RandomWalkOverlay

logger = logging.getLogger(__name__)


class GlitchImage(_Image):
    def __init__(self, *args):
        """ Construct a GlitchImage from either an image path, or a data frame """
        # pylint: disable=no-else-raise
        super().__init__()

        if len(args) > 1:
            raise Exception("Too many arguments provided.")
        else:
            arg = args[0]
            if isinstance(arg, str):
                logger.debug("GlitchImage from path {}".format(arg))
                self._load_from_path(arg)
            elif isinstance(arg, np.ndarry):
                logger.debug("GlitchImage from data with shape {}".format(arg.shape))
                self._load_from_data(arg)
            else:
                raise Exception("Argument must be type string or ndarray.")

        logger.info(
            f"GlitchImage@{id(self)}: width: {self.width}, height: {self.height}"
        )

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
        feed = GlitchImageFeed(self)
        return FreqModOverlay(feed, **kwargs)

    def random_walk_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        feed = GlitchImageFeed(self)
        return RandomWalkOverlay(feed, **kwargs)
