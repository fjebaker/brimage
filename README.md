# BRImage
Glitch art servlet. Python backend for manipulating images to create glitch-art effects inspired by CRT monitors.

## Installation and use
Requires Python3. First, clone the repository
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

## Sample image:

Input Image            |  Output Image
:-------------------------:|:-------------------------:
![](https://github.com/Dustpancake/BRImage/blob/master/sample-image.jpg)  |  ![](https://github.com/Dustpancake/BRImage/blob/master/sample-glitch.jpg)
