# BRImage
Glitch art servlet. Python backend for manipulating images to create glitch-art effects inspired by CRT monitors.

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
```
brimage -h
```

### pypi <a name="toc-sub-tag-1"></a>
I've made the project available with `pip` (you can view the project [here](https://pypi.org/project/BRImage/)):
```
pip install BRImage
```

### git <a name="toc-sub-tag-2"></a>
First, clone the repository
```bash
git clone https://github.com/Dustpancake/BRImage && cd BRImage
```
It is recommended to use a *virtual environment*
```bash
# *nix
python3 -m venv venv && source venv/bin/activate
```

- Installation

The installation is self contained in `setup.py`
```bash
python setup.py install 
```

- Running the script

To run, edit `run.py` to setup a BRImage overlay pipeline (docs and examples coming soon), and run
```
python run.py
```

## Sample image: <a name="toc-sub-tag-3"></a>

Input Image            |  Output Image
:-------------------------:|:-------------------------:
![](https://github.com/Dustpancake/BRImage/blob/master/sample-image.jpg)  |  ![](https://github.com/Dustpancake/BRImage/blob/master/sample-glitch.jpg)
