from BRImage.overlays.glitch import GOverlay
from BRImage.overlays.structures.glitchline import GL

class LinearOverlay(GOverlay):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def _divide_lines(self, nlines, lwidth=2):
		gls = []
		for i in range(nlines):
			gls.append(GL(int(i * self.width / nlines), lwidth, self.width, self.height))

		gls[0].assign_neighbours(None, gls[1])
		for i in range(1, len(gls)-1):
			gls[i].assign_neighbours(gls[i-1], gls[i+1])
		gls[-1].assign_neighbours(gls[-2], None)

		self._glines = gls


	def calc_straight_lines(self, *args, **kwargs):
		self._divide_lines(*args, **kwargs)
		for i in self._glines:
			i.schema = self.schema
			i.v_trace()

	def draw_straight_lines(self, *args, **kwargs):
		self.calc_straight_lines(*args, **kwargs)
		self.draw_lines()