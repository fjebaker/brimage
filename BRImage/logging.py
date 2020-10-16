import logging
import os

_LEVEL_ENCODING = {
    "DEBUG": "\U0001F41B  ",
    "INFO": "",
    "WARNING": "\U0001F440  ",
    "ERROR": "\U0001F6A8  ",
    "CRITICAL": "\U0001F480  ",
}


class CLIFormatter(logging.Formatter):
    def format(self, record):
        emoji = _LEVEL_ENCODING[record.levelname]
        s = f"{emoji}{record.msg}"
        return s


def _configure_logging(level, show=False):
    logger = logging.getLogger("brimage")
    if show:
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        handler = logging.StreamHandler()
        handler.setLevel(level)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


def _cli_logger():
    console_logger = logging.getLogger("brimagecli")

    cl_handler = logging.StreamHandler()
    cl_handler.setFormatter(CLIFormatter())
    console_logger.addHandler(cl_handler)
    console_logger.setLevel(logging.INFO)

    return console_logger


brimage_logger = _configure_logging(logging.DEBUG, show=False)
cli_logger = _cli_logger()
