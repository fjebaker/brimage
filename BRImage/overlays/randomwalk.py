import numpy as np

from BRImage.overlays.base_overlay import BaseOverlay
from BRImage.clib.algorithms import (
    MonochomeCanvas,
    RGBCanvas,
    random_walk_monochrome,
    random_walk_rgb,
)

import resource
from BRImage.logger import cli_logger

import logging

logger = logging.getLogger(__name__)


def print_memory_usage():
    logger.debug(
        "Memory usage at {} M".format(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000 ** 2
        )
    )


class RandomWalkOverlay(BaseOverlay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # fix: add border to prevent seg fault
        self._expand(100)  #  fix for some segfaults in randomwalk
        self._make_canvas()

    def map_random_walk(self, lines=500, greyscale=False):
        # convert to grey scale; colour is TODO
        image = self.image

        if greyscale:
            reference = self._get_gimage_data()
            imagee = np.mean(image, axis=2)
            # lower arrays into clib
            ref_canvas = MonochomeCanvas(reference)
            img_canvas = MonochomeCanvas(image)
            _random_walk_func = random_walk_monochrome
        else:
            reference = self._get_gimage_data("RGB")
            # lower arrays into clib
            ref_canvas = RGBCanvas(reference)
            img_canvas = RGBCanvas(image)
            _random_walk_func = random_walk_rgb

        print_memory_usage()
        cli_logger.info("Drawing lines...")

        quartile = int(lines/4)
        quartile_count = 0
        for i in range(lines):
            #  have to use print() for carriage return
            if i % quartile == 0:
                quartile_count += 25
                cli_logger.info(f"{quartile_count}% done...")
            _random_walk_func(ref_canvas, img_canvas)

        cli_logger.info(f"Drawing lines 100% done!")
        print_memory_usage()

        self.image = image
