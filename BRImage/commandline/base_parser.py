import argparse
import os
import time

from BRImage import VERSION, HEADER
from BRImage.glitchimage import GlitchImage
from BRImage.logging import cli_logger, brimage_logger

cli = argparse.ArgumentParser(
    prog="BRImage",
    description=f"CLI for BRImage library {VERSION}.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
sub_parser = cli.add_subparsers(dest="subcommand")
command_lookup = {}

cli.add_argument("--version", action="version", version="%(prog)s v" + VERSION)


def check_file_exists(file):
    """ check file exists; raise exception if not """
    if not os.path.isfile(file):
        exc_string = f"input file '{file}' does not exist."
        cli_logger.fatal(exc_string)
        raise Exception(exc_string)


def _add_image_io(parser):
    parser.add_argument(
        "input_image",
        type=str,
        help="Input image path; most common formats are accepted.",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default="output.jpg",
        help="Output image path.",
    )


def _image(parser, _runner):
    _add_image_io(parser)

    def image_run(args):
        # print since not needed anywhere in logs really
        print(HEADER)

        start = time.time()

        check_file_exists(args.input_image)
        gi = GlitchImage(args.input_image)

        cli_logger.info("\U0001F3A8 {}".format(gi))

        out = _runner(gi, **vars(args))
        cli_logger.info("Saving output file as '{}'...".format(args.output_file))
        out.save(args.output_file)

        end = time.time()
        cli_logger.info("\U0001F550 Time elapsed {0:.3f} seconds.".format(end - start))
        cli_logger.info("\U00002728 Done. \U00002728")

    return image_run


def subcommand(name, iotype="image", parent=sub_parser):
    brimage_logger.debug(f"Installing subcommand {name}, iotype '{iotype}'")

    def _wrap(func):
        parser = parent.add_parser(
            name,
            description=func.__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        _runner = func(parser)
        if iotype == "image":
            runner = _image(parser, _runner)
        else:
            exc_string = "Unknown iotype for subcommand {}".format(iotype)
            brimage_logger.fatal(exc_string)
            raise ValueError(exc_string)
        parser.set_defaults(runner=runner)

    return _wrap
