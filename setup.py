from setuptools import setup, Extension
import os

algorithms = Extension(
	'algorithms', 
	sources=[
		os.path.join('BRImage', 'lib', 'br_algorithms.c'),
		os.path.join('BRImage', 'lib', 'freqmod.c')
	],
	include_dirs = [
		os.path.join('BRImage', 'lib')
	]
)

setup(
	name='BRImage',
	version='0.1.0',
	description='Glitch ART Toolkit mimicking CRT monitor defects.',
	author='Dustpancake',
	url='https://github.com/Dustpancake/BRImage',
	packages=[
		'BRImage', 
		'BRImage.glitchcore', 
		'BRImage.overlays',
		'BRImage.overlays.structures'
	],
	install_requires=[
		'numpy==1.18.2',
		'scikit-image==0.16.2',
		'scipy==1.4.1',
		'matplotlib==3.2.1'
	],
	ext_package='__brimage_lib',
	ext_modules=[
		algorithms
	],
	zip_safe=False
)
