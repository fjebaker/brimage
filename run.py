from BRImage.glitchcore import *
import random
import numpy as np

import matplotlib.pyplot as plt
path = "sample-image.jpg"

fig = plt.figure()
ax = plt.gca()

gi = GImage(path)
print(gi)
lo = gi.linear_overlay(rinit=64, ginit=64, binit=64)
lo.schema = gi.get_colour_schema()
lo.calc_straight_lines(300, lwidth=1)

def l_r(x, y, scale):
	scale = (np.mean(scale) / 255)
	scale = scale**1.5 * 1.09
	return int(random.choice([-1, 1]) * random.random() * scale)

#lo.map_distort_all(l_r)
lo.map_single_cascade(l_r, refindex='fst', update_colour=False, restoring=1.5, damping=1.02, scaling_factor=0.5, diffmap_factor=1.01, damping_decay=-0.00001)
lo.draw_lines()

lo.show(ax, interpolation='nearest')
plt.show()