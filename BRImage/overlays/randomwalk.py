from BRImage.glitchcore import OverlayBase
from BRImage.clib.algorithms import random_walk, Canvas

import resource
def print_memory_usage():
    print("Memory usage at {} M".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000**2))

import numpy as np

class RandomWalkOverlay(OverlayBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def map_random_walk(self, lines=500):
        # convert to grey scale; colour is TODO
        self.expand(100)
        reference = np.array(
            self._gimage.get_image().convert("L")
        )
        image = np.array(
            self._image.convert("L")
        )

        # lower arrays into clib
        ref_canvas = Canvas()
        ref_canvas.set_inplace_layer(reference)
        img_canvas = Canvas()
        img_canvas.set_inplace_layer(image)

        print_memory_usage()
        import time
        start = time.time()
        for i in range(lines):
            print("Drawing lines {}".format(i), end="\r")
            random_walk(ref_canvas, img_canvas)
        end = time.time()

        print("Drawing lines {}".format(lines))
        print("Elapsed time {}".format(end - start))
        print("Done.")
        print_memory_usage()

        self._image = image
