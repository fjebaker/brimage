import abc

class BaseFeed(abc.ABC):
    """ Abstract class for providing data feeds """

    width: int
    height: int

    def __init__(self):
        ...

    def _as_array(self, colourfmt):
        """ Returns np array of image-like data: colourfmt can be L for greyscale or RGB for RGB"""
        ...

    def apply(self, new_image):
        """ Propage the distorted image back up to the feed """
        ...

    def expand(self, width, colours):
        """ Placeholder until I fix the seg fault bug in random walk """
        ...