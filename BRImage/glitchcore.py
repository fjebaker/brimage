import PIL
import skimage
from BRImage.glitchline import GL

class Schema:
	def __init__(self, im):
		self._im = im

	def __call__(self, x, y):
		return self._im.getpixel((x, y))

class _Image:
	def __init__(self):
		pass

	def show(self, ax, **kwargs):
		ax.imshow(self._image, **kwargs)

	def map_distort_all(self, scaling_function):
		for i in self._glines:
			i.distort(scaling_function)

	def map_single_cascade(self, scaling_function, refindex='mid', **kwargs):
		if refindex == 'mid':
			reference = self._glines[len(self._glines)//2]
		elif refindex == 'end':
			reference = self._glines[-1]
		elif refindex == 'fst':
			reference = self._glines[0]
		else:
			raise Exception("Unknown reference index '{}' -- available are 'mid', 'end', 'fst'.".format(refindex))
		if 'update_colour' in kwargs:
			reference.distort(scaling_function, kwargs['update_colour'])
		else:
			reference.distort(scaling_function)
		reference.cascade_copy(scaling_function, **kwargs)

	def draw_lines(self):
		array_image = self._image.load()
		for i in self._glines:
			i.draw(array_image)


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


class LinearOverlay(GOverlay):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	def calc_straight_lines(self, *args, **kwargs):
		self._divide_lines(*args, **kwargs)
		for i in self._glines:
			i.schema = self.schema
			i.v_trace()

	def draw_straight_lines(self, *args, **kwargs):
		self.calc_straight_lines(*args, **kwargs)
		self.draw_lines()


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