# BRImage
![Build](https://github.com/dustpancake/BRImage/workflows/Build/badge.svg)
[![PyPI Version](https://badge.fury.io/pypi/BRImage.svg)](https://pypi.python.org/pypi/BRImage/)

Glitch Art Library and command line tool for generating glitch-art effects inspired by CRT monitors.
One-liner install (requires Python >=3.7)
```
pip install BRImage && brimage -h
```

<!--BEGIN TOC-->
## Table of Contents
1. [Installation and use](#toc-sub-tag-0)
	1. [pypi](#toc-sub-tag-1)
	2. [git](#toc-sub-tag-2)
2. [Sample image:](#toc-sub-tag-3)
<!--END TOC-->

## Installation and use <a name="toc-sub-tag-0"></a>
BRImage now comes with a very minimal command line interface, usable with
```bash
brimage -h
```

### pypi <a name="toc-sub-tag-1"></a>
I've made the project available with `pip` (you can view the project [here](https://pypi.org/project/BRImage/)):
```bash
pip install BRImage
```

and run with
```bash
brimage
```

### Building from source <a name="toc-sub-tag-2"></a>
Requires [SWIG](http://swig.org/).

First, clone the repository
```bash
git clone https://github.com/Dustpancake/BRImage && cd BRImage
```
It is recommended to use a *virtual environment*
```bash
# *nix
python3 -m venv venv && source venv/bin/activate
```

Generate the SWIG files; for this we require `numpy.i`:
```bash
curl "https://raw.githubusercontent.com/numpy/numpy/master/tools/swig/numpy.i" > BRImage/clib/numpy.i
```
Then we generate the `.py` and `.cxx` files with
```bash
cd BRImage/clib \
    && swig -c++ -python -py3 algorithms.i \
    && cd -
```
We then build with
```bash
python setup.py build_ext --inplace
```

or install into the environment with 
```bash
pip install .
```
- Running the script

To run when build from source:
```bash
python BRImage
```

If installed, use
```bash
brimage
```

## Sample image: <a name="toc-sub-tag-3"></a>

Input Image            |  Output Image
:-------------------------:|:-------------------------:
![](https://github.com/Dustpancake/BRImage/blob/master/sample-image.jpg)  |  ![](https://github.com/Dustpancake/BRImage/blob/master/sample-glitch.jpg)
