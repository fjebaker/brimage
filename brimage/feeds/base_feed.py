import abc


class BaseFeed(abc.ABC):
    """ Abstract class for providing data feeds """

    width: int
    height: int

    def __init__(self):
        ...

    def as_array(self, colourfmt):
        """ Returns np array of image-like data: colourfmt can be L for greyscale or RGB for RGB. Will be called once per algorithm invocation."""
        # pylint: disable=unused-argument
        ...

    def apply(self, new_image):
        """ Propage the distorted image back up to the feed """
        # pylint: disable=unused-argument
        ...
