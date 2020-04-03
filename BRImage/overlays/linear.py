from BRImage.overlays.glitch import GOverlay

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