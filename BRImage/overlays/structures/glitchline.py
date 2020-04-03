import numpy as np

class GL:
	def __init__(self, startx, lwidth, im_width, im_height):
		self.startx = startx
		self.starty = 0
		self.endx = im_width
		self.endy = im_height
		self.lwidth = lwidth

		self._neighbours = [None, None]
		self.map = []						# [(posx, posy, colour), ...]
		self._mode = None
		self._schema = None
		self._diffmap = []

	def assign_neighbours(self, ln, rn):
		self._neighbours = [ln, rn]

	def set_mode(self, mode):
		self._mode = mode

	def v_trace(self):
		self.map = []
		schema = self.schema
		for y in range(self.starty, self.endy):
			self.map.append((self.startx, y, schema(self.startx, y)))

	def draw(self, image):
		for x, y, val in self.map:
			for dx in range(-self.lwidth, self.lwidth+1):
				try:
					image[x+dx, y] = val
				except:
					pass

	def _apply_diffmap(self, diffmap, direction, scaling_function, restoring=0, damping=0, scaling_factor=0, diffmap_factor=1, update_colour=True):
		# self._diffmap
		runningx = self.startx
		schema = self.schema

		if update_colour:
			newpt = lambda x, y, val: (x, y, schema(x, y))
		else:
			newpt = lambda x, y, val: (x, y, val)

		#if direction == 1:
		x_update = lambda x, y, i: x + ((diffmap_factor * diffmap[i]) + (scaling_function(*newpt(x, y, val)) * scaling_factor)) * damping
		#else:
			#x_update = lambda x, i: x - diffmap[i]

		new_map = []
		for i in range(len(self.map)):
			x, y, val = self.map[i]
			runningx = x_update(x, y, i)								# TODO
			try:
				new_map.append(newpt(runningx, y, val))
			except:
				pass
			self._diffmap.append(runningx - self.startx)
		self.startx = new_map[0][0]
		self.map = new_map

		# these two functions could be amalgamated?

	def distort(self, scaling_function, update_colour=True):
		self._diffmap = []
		runningx = self.startx
		schema = self.schema

		if update_colour:
			newpt = lambda x, y, val: (x, y, schema(x, y))
		else:
			newpt = lambda x, y, val: (x, y, val)

		new_map = []
		for (_, y, val) in self.map:
			runningx += scaling_function(runningx, y, val)
			try:
				new_map.append(newpt(runningx, y, val))
			except:
				pass
			self._diffmap.append(runningx - self.startx)
		self.startx = new_map[0][0]
		self.map = new_map

	def cascade_copy(self, scaling_function, **kwargs):
		self._cascade(1, scaling_function, **kwargs)
		self._cascade(0, scaling_function, **kwargs)

	def _cascade(self, direction, scaling_function, damping_decay=0, _counter=[0, 0], **kwargs):
		nline = self._neighbours[direction]
		if nline is None:
			return
		_counter[direction]+=1
		if 'damping' in kwargs:
			kwargs['damping'] *= np.exp(-1 * damping_decay * _counter[direction])
		if 'scaling_factor' in kwargs:
			kwargs['scaling_factor'] *= np.exp(-1 * damping_decay * _counter[direction])


		nline._apply_diffmap(self._diffmap, direction, scaling_function, **kwargs)
		nline._cascade(direction, scaling_function, _counter=_counter, **kwargs)

	@property
	def schema(self):
		if self._schema is None:
			raise Exception("Undefined colour schema")
		return self._schema

	@schema.setter
	def schema(self, schema):
		self._schema = schema