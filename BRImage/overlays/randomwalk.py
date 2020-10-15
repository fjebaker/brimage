from BRImage.glitchcore import OverlayBase
from BRImage.clib.algorithms import (
    MonochomeCanvas,
    RGBCanvas,
    random_walk_monochrome,
    random_walk_rgb,
)

import resource


def print_memory_usage():
    print(
        "Memory usage at {} M".format(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000 ** 2
        )
    )


import numpy as np


class RandomWalkOverlay(OverlayBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # fix: add border to prevent seg fault
        self.expand(100)

    def map_random_walk(self, lines=500, greyscale=False):
        # convert to grey scale; colour is TODO
        if greyscale:
            reference = np.array(self._gimage.get_image().convert("L"))
            image = np.array(self._image.convert("L"))
            # lower arrays into clib
            ref_canvas = MonochomeCanvas(reference)
            img_canvas = MonochomeCanvas(image)
            print_memory_usage()
            import time

            start = time.time()
            for i in range(lines):
                print("Drawing lines {}".format(i), end="\r")
                random_walk_monochrome(ref_canvas, img_canvas)
            end = time.time()
        else:
            reference = np.array(self._gimage.get_image().convert("RGB"))
            image = np.array(self._image.convert("RGB"))
            # lower arrays into clib
            ref_canvas = RGBCanvas(reference)
            img_canvas = RGBCanvas(image)
            print_memory_usage()
            import time

            start = time.time()
            for i in range(lines):
                print("Drawing lines {}".format(i), end="\r")
                random_walk_rgb(ref_canvas, img_canvas)
            end = time.time()

        print("Drawing lines {}".format(lines))
        print("Elapsed time {}".format(end - start))
        print("Done.")
        print_memory_usage()

        self._image = image
