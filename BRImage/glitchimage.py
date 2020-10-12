from BRImage.glitchcore import _Image
from BRImage.overlays import FreqModOverlay, RandomWalkOverlay

try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage


class GlitchImage(_Image):
    def __init__(self, path):
        self._path = path
        image = PILImage.open(path)
        self._image = image.convert("RGB")
        self.width, self.height = self._image.size

        # self.cols = self._reduced_im.convert('RGB').getcolors(256)

    def __str__(self):
        return "{}x{} GImage".format(self.width, self.height)

    def get_image(self):
        return self._image

    def freqmod_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        return FreqModOverlay(self, **kwargs)

    def random_walk_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        return RandomWalkOverlay(self, **kwargs)
