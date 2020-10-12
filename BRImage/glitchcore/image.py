import numpy as np

try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage


class _Image:
    def __init__(self):
        pass

    def show(self, ax, **kwargs):
        ax.imshow(self._image, **kwargs)

    def save(self, name, **kwargs):
        im = PILImage.fromarray(np.uint8(self._image))
        im.save(name)
