from BRImage.glitchimage import *
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
	scale = (np.mean(scale) / 255)
	scale = scale**1.5 * 3
	return int(random.choice([-1, 1]) * random.random() * scale)

def s_f(x, y, scale):
	return int(l_r(x, y, scale) / 2)

#lo.map_distort_all(l_r)
lo.map_single_cascade(l_r, 
	# shift_func=s_f,
	# shift_factor=1,
	refindex='mid', 
	update_colour=False, 
	restoring=1.5, 
	damping=1.02, 
	scaling_factor=0.5, 
	diffmap_factor=1.04, 
	damping_decay=-0.00001)
lo.draw_lines()

lo.show(ax, interpolation='nearest')
plt.show()