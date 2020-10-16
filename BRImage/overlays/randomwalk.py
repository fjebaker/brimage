import numpy as np

from BRImage.glitchcore import OverlayBase
from BRImage.clib.algorithms import (
    MonochomeCanvas,
    RGBCanvas,
    random_walk_monochrome,
    random_walk_rgb,
)

import resource
from BRImage.logging import brimage_logger, cli_logger


def print_memory_usage():
    brimage_logger.debug(
        "Memory usage at {} M".format(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000 ** 2
        )
    )


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
            _random_walk_func = random_walk_monochrome
        else:
            reference = np.array(self._gimage.get_image().convert("RGB"))
            image = np.array(self._image.convert("RGB"))
            # lower arrays into clib
            ref_canvas = RGBCanvas(reference)
            img_canvas = RGBCanvas(image)
            _random_walk_func = random_walk_rgb

        print_memory_usage()
        for i in range(lines):
            #  have to use print() for carriage return
            print("Drawing lines {}...".format(i), end="\r")
            # cli_logger.info("Drawing lines {}\r".format(i))
            _random_walk_func(ref_canvas, img_canvas)

        cli_logger.info("Drawing lines {}..!".format(lines))
        print_memory_usage()

        self._image = image
