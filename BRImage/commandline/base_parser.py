import argparse
import os

from BRImage import VERSION, HEADER
from BRImage.glitchimage import GlitchImage

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
        raise Exception(f"input file '{file}' does not exist.")


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

        print(HEADER)

        check_file_exists(args.input_image)
        gi = GlitchImage(args.input_image)

        print("[+] {}".format(gi))

        out = _runner(gi, **vars(args))
        out.save(args.output_file)

    return image_run


def subcommand(name, iotype="image", parent=sub_parser):
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
            raise ValueError("Unknown iotype for subcommand {}".format(iotype))
        parser.set_defaults(runner=runner)

    return _wrap
