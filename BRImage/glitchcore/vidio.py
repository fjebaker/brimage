import os
import fractions

import numpy as np


from BRImage.glitchcore.helper import get_temporary_directory
from BRImage.glitchcore.image import _Image

import logging

logger = logging.getLogger(__name__)

try:
    import ffmpeg
except:
    logger.fatal(
        (
            "No FFMPEG; for video IO brimage requires ffmepg. "
            "Get it here: "
            "https://ffmpeg.org/ "
            "and install the python wrapper library: "
            "python -m pip install ffmpeg-python"
        )
    )

    exit(1)


class VidIO(_Image):
    def __init__(self, path_to_video, num_frames=None, output_framerate=None):
        probe = ffmpeg.probe(path_to_video)
        video_stream = next(
            (stream for stream in probe["streams"] if stream["codec_type"] == "video"),
            None,
        )
        if video_stream == None:
            logger.warning("No stream found in input video.")
            self.width = 0
            self.height = 0
            self.native_framerate = 0
        else:
            self.width = int(video_stream["width"])
            self.height = int(video_stream["height"])
            self.native_framerate = float(
                fractions.Fraction(video_stream["r_frame_rate"])
            )

        logger.info(
            f"VidIO@{id(self)}: width: {self.width}, height: {self.height}, native_framerate: {self.native_framerate}"
        )

        self._num_frames = num_frames
        self.output_framerate = output_framerate
        self._path = path_to_video
        self._out_pipe = ""

    def output(self, filename):
        self._out_path = filename
        return self

    def __enter__(self):
        """ context managed image pipeline """
        if not self._out_path:
            exc_string = "No output file specified. Use .output(filname:str)"
            logger.error(exc_string)
            raise Exception(exc_string)

        logger.debug("Opening IO pipes...")
        self._in_pipe = self._open_input_pipeline()
        self._out_pipe = self._open_output_pipeline()

        logger.debug("IO pipes open, returning from __enter__")
        return self

    def _open_input_pipeline(self):
        # create input configuration dictionary
        in_config = dict(format="rawvideo", pix_fmt="rgb24")

        # add additional config
        if self._num_frames is not None:
            in_config["vframes"] = self._num_frames

        logger.debug(f"Input Configuration {in_config}")

        # open and return stream
        return (
            ffmpeg.input(self._path)
            .output("pipe:", **in_config)
            .run_async(pipe_stdout=True, pipe_stderr=True)
        )

    def _open_output_pipeline(self):
        # create output configuration dictionary
        out_config = dict(pix_fmt="yuv420p")

        # add additional config
        if self.output_framerate is None:
            self.output_framerate = self.native_framerate
        out_config["r"] = self.output_framerate

        logger.debug(f"Output Configuration {out_config}")

        #  open and return stream
        return (
            ffmpeg.input(
                "pipe:",
                format="rawvideo",
                pix_fmt="rgb24",
                s=f"{self.width}x{self.height}",
            )
            .output(self._out_path, **out_config)  # output must be yuv420p
            .overwrite_output()
            .run_async(pipe_stdin=True, pipe_stderr=True)
        )

    def __exit__(self, exc_type, exc_value, traceback):
        logger.debug("__exit__ called; closing pipes...")
        self._out_pipe.stdin.close()
        self._out_pipe.wait()
        self._in_pipe.wait()
        logger.debug("pipes closed.")

        if exc_type:
            logger.error(exc_value)
            logger.error(traceback)
            raise exc_value

    def _timestamp_offsets(self, counter):
        """ calculates the time stamp from the framerate of the source and destination stream """
        native_time = counter * 1 / self.native_framerate
        dest_time = counter * 1 / self.output_framerate
        return native_time, dest_time

    def __iter__(self):
        counter = 0
        logger.debug("Iterator started...")
        while True:
            counter += 1
            # logger.debug(f"Counter at {counter}")
            bytestream = self._in_pipe.stdout.read(
                self.width * self.height * 3  #  RGB frame
            )
            # logger.debug(f"read in {len(bytestream)} bytes")
            if bytestream:
                frame = np.frombuffer(bytestream, np.uint8).reshape(
                    [self.height, self.width, 3]
                )
                in_time, out_time = self._timestamp_offsets(counter)
                yield frame, in_time, out_time
            else:
                logger.debug("stream exhausted")
                break
        logger.debug("Iterator ended.")

    def save(self, frame):
        """ override: save the video from output frames """
        self._out_pipe.stdin.write(frame.astype(np.uint8).tobytes())
        # logger.debug("frame written to pipe")
