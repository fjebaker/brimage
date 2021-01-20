from brimage.feeds.base_feed import BaseFeed


class GlitchVideoFeed(BaseFeed):
    def __init__(self, gvideo):
        super().__init__()
        self.gvideo = gvideo

        self._staged_frame = None
        self._new_frame = None

    @property
    def width(self):
        return self.gvideo.width

    @property
    def height(self):
        return self.gvideo.height

    def stage(self, frame):
        self._staged_frame = frame

    def as_array(self, colourfmt):
        """ Get the next frame of the video stream """
        # pylint: disable=unused-argument
        return self._staged_frame

    def apply(self, new_image):
        """ Save the image frame """
        self._new_frame = new_image

    def expand(self, width, colours):
        #  deprecated: will be removed
        pass
