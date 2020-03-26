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
lo.calc_straight_lines(80, lwidth=1)

def l_r(x, y, scale):
	scale = 1 - (np.mean(scale) / 255)
	scale = scale**1.5 * 9
	return int(random.choice([-1, 1]) * random.random() * scale)

#lo.map_distort_all(l_r)
lo.map_single_cascade(l_r, refindex='mid', update_colour=False, restoring=1.5, damping=1.03, scaling_factor=0.4, diffmap_factor=1.01, damping_decay=0)
lo.draw_lines()

lo.show(ax)
plt.show()