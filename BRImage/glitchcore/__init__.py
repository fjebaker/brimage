from BRImage.glitchcore.base import _Image, remap

class Schema:
	""" colour schema class """
	def __init__(self, im):
		self._im = im

	def __call__(self, x, y):
		return self._im.getpixel((x, y))