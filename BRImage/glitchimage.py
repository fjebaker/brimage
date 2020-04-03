import PIL
import skimage
from BRImage.glitchcore import _Image, Schema
from BRImage.overlays import LinearOverlay

class GImage(_Image):
	def __init__(self, path, ncolors=4):
		self._path = path
		image = PIL.Image.open(path)
		self._image = image.convert('RGB')
		self._reduced_im = image.convert('P', palette=PIL.Image.ADAPTIVE, colors=ncolors)

		self._ncolors = ncolors
		self.width, self.height = self._image.size

		self.cols = self._reduced_im.convert('RGB').getcolors(256)

	def linear_overlay(self, **kwargs):
		return LinearOverlay(self, self.width, self.height, **kwargs)

	def get_default_schema(self):
		return Schema(self._reduced_im.convert('RGB'))

	def get_colour_schema(self):
		return Schema(self._image)

	def __str__(self):
		return "{}x{} GImage with {} colors".format(self.width, self.height, self._ncolors)

	def show_reduced(self, ax):
		ax.imshow(self._reduced_im)