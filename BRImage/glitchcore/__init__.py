from BRImage.glitchcore.base import _Image

def remap(x, s1, s2, d1, d2):
	""" helper functio: remaps x in range s1-s2 into d1-d2 """
	return (((x-s1)/(s2-s1)) * (d2-d1)) + d1

class Schema:
	""" colour schema class """
	def __init__(self, im):
		self._im = im

	def __call__(self, x, y):
		return self._im.getpixel((x, y))