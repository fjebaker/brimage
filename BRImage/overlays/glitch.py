import PIL
from BRImage.glitchcore.base import _Image
from BRImage.overlays.structures.glitchline import GL

class GOverlay(_Image):
	def __init__(self, gimage, width, height, rinit=255, ginit=255, binit=255):
		self._gimage = gimage

		self.width, self.height = width, height
		self._image = PIL.Image.new('RGB', [width, height], (rinit, ginit, binit))

		self._schema = None

	def _divide_lines(self, nlines, lwidth=2):
		gls = []
		for i in range(nlines):
			gls.append(GL(int(i * self.width / nlines), lwidth, self.width, self.height))

		gls[0].assign_neighbours(None, gls[1])
		for i in range(1, len(gls)-1):
			gls[i].assign_neighbours(gls[i-1], gls[i+1])
		gls[-1].assign_neighbours(gls[-2], None)

		self._glines = gls

	@property
	def schema(self):
		if self._schema is None:
			return self._gimage.get_default_schema()
		return self._schema
	
	@schema.setter
	def schema(self, schema):
		self._schema = schema