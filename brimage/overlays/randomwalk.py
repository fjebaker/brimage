import resource
import functools
import random
import logging

import numpy as np

from brimage.overlays.base_overlay import BaseOverlay
from brimage.clib.algorithms import (
    MonochomeCanvas,
    RGBCanvas,
    random_walk_monochrome,
    random_walk_rgb,
)
from brimage.logger import cli_logger

logger = logging.getLogger(__name__)


def print_memory_usage():
    logger.debug(
        "Memory usage at {} M".format(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000 ** 2
        )
    )


@functools.lru_cache(None)
def _get_init_point(_, x_max, y_max):
    """ Generates initializing points for the random walk; caches so that they are always the same for a given session """
    x, y = random.randint(0, x_max - 1), random.randint(0, y_max - 1)
    return x, y


class RandomWalkOverlay(BaseOverlay):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def map_algorithm(self, **kwargs):
        # unpack
        lines = kwargs.get("lines", 500)
        greyscale = kwargs.get("greyscale", False)

        # convert to grey scale; colour is TODO

        # fix: add border to prevent seg fault
        self._make_canvas()

        image = self.image

        if greyscale:
            reference = self._get_from_feed()
            image = np.mean(image, axis=2)

            # lower arrays into clib
            ref_canvas = MonochomeCanvas(reference)
            img_canvas = MonochomeCanvas(image)
            _random_walk_func = random_walk_monochrome
        else:
            reference = self._get_from_feed("RGB")
            # lower arrays into clib
            ref_canvas = RGBCanvas(reference)
            img_canvas = RGBCanvas(image)
            _random_walk_func = random_walk_rgb

        print_memory_usage()
        cli_logger.info("Drawing lines...")

        quartile = int(lines / 4)
        quartile_count = 0
        for i in range(lines):
            #  have to use print() for carriage return
            if i % quartile == 0:
                quartile_count += 25
                cli_logger.info(f"{quartile_count}% done...")
            x, y = _get_init_point(i, self.width, self.height)
            _random_walk_func(ref_canvas, img_canvas, x, y)

        cli_logger.info(r"Drawing lines 100% done!")
        print_memory_usage()

        self.image = image

        return self.image
