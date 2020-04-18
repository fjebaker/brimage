import numpy as np

try:
    import Image as PILImage
except ImportError:
    from PIL import Image as PILImage


def remap(x, s1, s2, d1, d2):
	""" helper functio: remaps x in range s1-s2 into d1-d2 """
	return (((x-s1)/(s2-s1)) * (d2-d1)) + d1


class _Image:
	def __init__(self):
		pass

	def show(self, ax, **kwargs):
		ax.imshow(self._image, **kwargs)

	def save(self, name, **kwargs):
		im=PILImage.fromarray(np.uint8(self._image))
		im.save(name)

		#matplotlib.image.imsave(name, self._image, **kwargs)

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