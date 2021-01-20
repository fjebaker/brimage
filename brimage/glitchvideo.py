from brimage.glitchcore.vidio import _VidIO
from brimage.feeds import GlitchVideoFeed

from brimage.overlays import FreqModOverlay, RandomWalkOverlay

import logging

logger = logging.getLogger(__name__)


class GlitchVideo(_VidIO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._out_path = ""

        self.algol_args = []
        self.algol_kwargs = {}

    def set_output(self, path):
        logger.debug("Updated output path to {}".format(path))
        self._out_path = path

    def set_background_colour(self, r, g, b):
        self._rinit = r
        self._ginit = g
        self._binit = b

    def _do_mapping(self, Overlay):

        if self._out_path is None:
            raise Exception("No output path defined.")

        logger.info("Saving output video as {}".format(self._out_path))
        logger.info("Running for {} frames".format(self._num_frames))

        logger.debug("Creating video feed")

        feed = GlitchVideoFeed(self)
        algorithm = Overlay(
            feed, rinit=self._rinit, ginit=self._ginit, binit=self._binit
        )

        with self.output(self._out_path) as i_stream:

            for frame, i_time, o_time in i_stream:

                feed.stage(frame)  #  load frame as next item

                # call method
                new_frame = algorithm.map_algorithm(
                    *self.algol_args, **self.algol_kwargs
                )

                # need to call to convert back to rgb but it's also kind of fun to comment this line out ;)
                new_frame = algorithm._to_rgb()

                self.save(new_frame)

        logging.info("Finished processing video")

    def map_freqmod(self, *args, **kwargs):
        self.algol_args = args
        self.algol_kwargs = kwargs

        self._do_mapping(FreqModOverlay)
        return self  #  for politeness :)

    def map_randomwalk(self, *args, **kwargs):
        self.algol_args = args
        self.algol_kwargs = kwargs

        self._do_mapping(RandomWalkOverlay)
        return self

    def map_freqmod_audio(self, freqmod_audio_mapping, *args):
        raise NotImplementedError
