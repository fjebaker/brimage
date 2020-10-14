from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from BRImage import VERSION
import os

import numpy as np

algorithms = Extension(
    "BRImage.clib._algorithms",
    sources=[
        os.path.join("BRImage", "clib", "freqmod.cpp"),
        os.path.join("BRImage", "clib", "randomwalk.cpp"),
        os.path.join("BRImage", "clib", "canvas", "subcanvas.cpp"),
        os.path.join("BRImage", "clib", "canvas", "canvas.cpp"),
        os.path.join("BRImage", "clib", "shapes", "coord.cpp"),
        os.path.join("BRImage", "clib", "shapes", "shapes.cpp"),
        os.path.join("BRImage", "clib", "algorithms_wrap.cxx"),
    ],
    language="c++",
    extra_compile_args=["-std=c++17"],
    include_dirs=[np.get_include()],
)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="BRImage",
    version=VERSION,
    description="Glitch Art Toolkit mimicking CRT monitor defects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dustpancake",
    url="https://github.com/Dustpancake/BRImage",
    entry_points={
        "console_scripts": [
            "brimage = BRImage.__main__:main",
        ],
    },
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.2",
        "scipy>=1.4.1",
        "Pillow>=7.1.1",
        "wheel>=0.34.2",
        "setuptools>=46.1.3",
    ],
    ext_modules=[algorithms],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.7",
    zip_safe=False,
)
