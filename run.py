from BRImage.glitchimage import *
import random
import numpy as np

import matplotlib.pyplot as plt
path = "sample-image.jpg"

gi = GImage(path)
print(gi)
fm = gi.freqmod_overlay(rinit=0, ginit=0, binit=0)
fm.schema = gi.get_colour_schema()
fm.map_freq_modulation(omega=0.1, phase=0.1, lowpass=0.2)
fm.post_quantize(6)

fm.save("sample-glitch.jpg")
