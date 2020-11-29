<p align="center">
  <img alt="BRImage" src="https://github.com/Dustpancake/BRImage/blob/master/banner-image.jpg">
</p>


# BRImage

<p align="center">
<a href="https://github.com/dustpancake/BRImage/workflows/Build/"><img alt="Build Status" src="https://github.com/dustpancake/BRImage/workflows/Build/badge.svg"></a>
<a href="https://pypi.python.org/pypi/BRImage/"><img alt="PyPi Version" src="https://img.shields.io/pypi/v/brimage.svg"></a>
<a href="https://pypi.python.org/pypi/BRImage/"><img alt="Downloads per Week" src="https://img.shields.io/pypi/dw/brimage.svg"></a>
</p>


Glitch Art Library and command line tool for generating glitch-art effects inspired by CRT monitors.

One-liner install:
```
pip install BRImage && brimage -h
```
*Note:* requires Python3.7 or higher.

<!--BEGIN TOC-->
## Table of Contents
1. [Usage](#toc-sub-tag-0)
	1. [Frequency Modulation](#toc-sub-tag-1)
	2. [Random Walk](#toc-sub-tag-2)
2. [Installation](#toc-sub-tag-3)
	1. [pypi](#toc-sub-tag-4)
	2. [Building from source](#toc-sub-tag-5)
3. [Changelog](#toc-sub-tag-6)
<!--END TOC-->

## Usage <a name="toc-sub-tag-0"></a>
BRImage can be used as both a command line interface and python package. The command line tool provides basic access to each algorithm.

```bash
brimage -h
```

### Frequency Modulation <a name="toc-sub-tag-1"></a>
Command line:
```
$ brimage freqmod -h
usage: BRImage freqmod [-h] [--omega OMEGA] [--phase PHASE] [--lowpass LOWPASS] [--pquantize PQUANTIZE] [-o OUTPUT_FILE] input_image

Frequency modulation algorithm for images. Implicitly converts to greyscale.

positional arguments:
  input_image           Input image path; most common formats are accepted.

optional arguments:
  -h, --help            show this help message and exit
  --omega OMEGA         Frequency omega; controls line spacing. Range: 0.0 to 1.0, >1.0 also works, but ugly. (default: 0.3)
  --phase PHASE         Controls the phase range that is used to map the pixel values into. Higher values distort the image more. Range: 0.0 to 1.0 (default: 0.5)
  --lowpass LOWPASS     Set the lowpass filter amount. Lower values blur out fine detail more. Set to 0 disables the filter. Preconfigured to 30Hz sample rate. Range: 0.0 to 1.0. (default: 0)
  --pquantize PQUANTIZE
                        Post-quantize number; integer number of colours to quantize image to after frequency modulation. Range: >=0. Value of 0 disables post-quantize (default: 0)
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output image path. (default: output.jpg)
```
Example:

Input Image            |  Output Image
:-------------------------:|:-------------------------:
![](https://github.com/Dustpancake/BRImage/blob/master/examples/sample-image.jpg)  |  ![](https://github.com/Dustpancake/BRImage/blob/master/examples/freqmod.jpg)

### Random Walk <a name="toc-sub-tag-2"></a>
Command line:
```
$ brimage randomwalk -h
usage: BRImage randomwalk [-h] [--lines LINES] [--greyscale] [-o OUTPUT_FILE] input_image

Random walk algorithm for images. Most values are still hardcoded in a header file, which requires recompilation. Later release will make this available through python.

positional arguments:
  input_image           Input image path; most common formats are accepted.

optional arguments:
  -h, --help            show this help message and exit
  --lines LINES         Number of individual line paths to draw. (default: 500)
  --greyscale           Process image as greyscale. (default: False)
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Output image path. (default: output.jpg)
```
Example:

Input Image            |  Output Image
:-------------------------:|:-------------------------:
![](https://github.com/Dustpancake/BRImage/blob/master/examples/sample-image.jpg)  |  ![](https://github.com/Dustpancake/BRImage/blob/master/examples/randomwalk.jpg)

## Installation <a name="toc-sub-tag-3"></a>

### pypi <a name="toc-sub-tag-4"></a>
I've made the project available with `pip` (you can view the project [here](https://pypi.org/project/BRImage/)):
```bash
pip install BRImage
```

and run with
```bash
brimage
```

### Building from source <a name="toc-sub-tag-5"></a>
- Requires [SWIG](http://swig.org/).

First, clone the repository
```bash
git clone https://github.com/Dustpancake/BRImage && cd BRImage
```

Generate the SWIG files; for this we require `numpy.i`:
```bash
curl "https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i" > BRImage/clib/numpy.i
```
Then we generate the `.py` and `.cxx` files with
```bash
swig -c++ -python -py3 BRImage/clib/algorithms.i
```
The next stage can be done in a few different ways:

- Isolated `build` directory

Build the project with the `--target` pip flag, to prevent it from being installed into the environment:
```bash
pip install --target build .
```
alternatively, use the develop mode
```
pip install -e .
```

- Install dependencies and build inplace:

Install the required modules with
```bash
pip install -r requirements.txt
```
Then to only build the external C++ modules, use
```bash
python setup.py build_ext --inplace
```
Run with
```bash
python BRImage
```

## Changelog <a name="toc-sub-tag-6"></a>

- 0.2.2: Fixed segfault related bugs; cleaned code and implemented random walk for video feeds.
- 0.2.1: Finished the video input feeds, and implementation for the frequency modulation part of video glitches. No CLI options for this available yet.
- 0.2.0: Major refactor, favouring Feed derived classes as abstraction for image input.
- 0.1.11: Staged some video I/O wrappers.
- 0.1.10: Introduced `numdevs` contrasting parameter in frequency modulation.
- 0.1.9: Updated CLI for all algorithms.
- 0.1.8: RGB support added for random walk.
- 0.1.7: Added random walk algorithm (greyscale only).
- 0.1.6: Changed home-baked to SWIG wrapper.
- 0.1.5: Home-baked C++ backend for the frequency modulation algorithm.

---

Uses [ffmeg](https://github.com/kkroening/ffmpeg-python) for Video I/O, [pillow](https://github.com/python-pillow/Pillow) for Image I/O, [numpy](https://github.com/numpy/numpy) as the workhorse and [black](https://github.com/psf/black) for formatting.

---


Todo:

- phase damping option on frequency modulation
- seed points for random walk