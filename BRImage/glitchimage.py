from BRImage.glitchcore import _Image
from BRImage.overlays import FreqModOverlay

try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage

class GlitchImage(_Image):

    def __init__(self, path, ncolors=4):
        self._path = path
        image = PILImage.open(path)
        self._image = image.convert('RGB')
        self._reduced_im = image.convert('P', palette=PILImage.ADAPTIVE, colors=ncolors)

        self._ncolors = ncolors
        self.width, self.height = self._image.size

        self.cols = self._reduced_im.convert('RGB').getcolors(256)

    def __str__(self):
        return "{}x{} GImage with {} colors".format(self.width, self.height, self._ncolors)

    def show_reduced(self, ax):
        ax.imshow(self._reduced_im)

    def get_image(self):
        return self._image

    def freqmod_overlay(self, **kwargs):
        """ frequency modulation overlay getter """
        return FreqModOverlay(self, **kwargs)
