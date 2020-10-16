from BRImage.commandline.base_parser import subcommand
from BRImage.logging import cli_logger


def _run(ginput, omega=0.3, phase=0.5, lowpass=0, pquantize=0, **kwargs):
    """ run frequency modulation cli script """
    cli_logger.info(
        f"Frequency modulation with omega {omega:.3f}, phase {phase:.3f}, lowpass {lowpass:.3f}, pquantize {pquantize}."
    )
    fm = ginput.freqmod_overlay(rinit=0, ginit=0, binit=0)
    fm.map_freq_modulation(omega=omega, phase=phase, lowpass=lowpass)
    if pquantize > 0:
        fm.post_quantize(pquantize)
    fm.apply()
    return ginput


@subcommand("freqmod")
def _freqmod_cli(parser):
    """ Frequency modulation algorithm for images. Implicitly converts to greyscale. """
    parser.add_argument(
        "--omega",
        type=float,
        default=0.3,
        help="Frequency omega; controls line spacing. Range: 0.0 to 1.0, >1.0 also works, but ugly.",
    )
    parser.add_argument(
        "--phase",
        type=float,
        default=0.5,
        help="Controls the phase range that is used to map the pixel values into. Higher values distort the image more. Range: 0.0 to 1.0",
    )
    parser.add_argument(
        "--lowpass",
        type=float,
        default=0,
        help="Set the lowpass filter amount. Lower values blur out fine detail more. Set to 0 disables the filter. Preconfigured to 30Hz sample rate. Range: 0.0 to 1.0.",
    )
    parser.add_argument(
        "--pquantize",
        type=int,
        default=0,
        help="Post-quantize number; integer number of colours to quantize image to after frequency modulation. Range: >=0. Value of 0 disables post-quantize",
    )

    return _run
