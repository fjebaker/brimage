from BRImage.overlays.structures import _Overlay
import PIL

class GOverlay(_Overlay):
	def __init__(self, gimage, width, height, rinit=255, ginit=255, binit=255):
		self._gimage = gimage

		self.width, self.height = width, height
		self._image = PIL.Image.new('RGB', [width, height], (rinit, ginit, binit))

		self._schema = None