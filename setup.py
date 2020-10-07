from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from BRImage import VERSION
import os

algorithms = Extension(
	'BRImage.clib._algorithms',
	sources=[
		os.path.join('BRImage', 'clib', 'freqmod.cpp'),
		os.path.join('BRImage', 'clib', 'algorithms_wrap.cxx'),
	],
	language='c++'
)

with open('README.md', 'r') as f:
	long_description=f.read();


class BuildWithNumpy(build_ext):
    """ build_ext command with numpy headers  """
    def run(self):
        import numpy

        self.include_dirs.append(numpy.get_include())
        build_ext.run(self)

setup(
	name='BRImage',
	version=VERSION,
	description='Glitch Art Toolkit mimicking CRT monitor defects.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Dustpancake',
	url='https://github.com/Dustpancake/BRImage',
	entry_points={
	    'console_scripts': [
	        'brimage = BRImage.__main__:main',
	    	],
	},
	packages=find_packages(),
	install_requires=[
		'numpy>=1.18.2',
		'scipy>=1.4.1',
		'Pillow>=7.1.1',
		'wheel>=0.34.2',
		'setuptools>=46.1.3'
	],
	cmdclass={
		'build_ext': BuildWithNumpy
	},
	ext_modules=[
		algorithms
	],
	classifiers=[
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	],
	python_requires=">=3.7",
	zip_safe=False
)
