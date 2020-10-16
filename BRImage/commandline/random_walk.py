from BRImage.commandline.base_parser import subcommand
from BRImage.logging import cli_logger


def _run(ginput, lines=500, greyscale=False, **kwargs):
    """ run random walk cli script """
    cli_logger.info(
        "Random walk: drawing {} lines, {} mode.".format(
            lines, "greyscale" if greyscale else "colour"
        )
    )
    rw = ginput.random_walk_overlay(rinit=35, ginit=32, binit=28)
    rw.map_random_walk(lines=lines, greyscale=greyscale)
    rw.apply()
    return ginput


@subcommand("randomwalk")
def _randomwalk_cli(parser):
    """ Random walk algorithm for images. Most values are still hardcoded in a header file, which requires recompilation. Later release will make this available through python."""
    parser.add_argument(
        "--lines",
        type=int,
        default=500,
        help="Number of individual line paths to draw.",
    )
    parser.add_argument(
        "--greyscale", action="store_true", help="Process image as greyscale."
    )

    return _run
