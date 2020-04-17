""" command line interface for using BRImage """ 
import argparse
import os

from BRImage.glitchimage import *
from BRImage import VERSION, HEADER

def run_fm(path, omega, phase, lowpass, output_file):
	""" run frequency modulation cli script """
	gi = GImage(path)
	print("[+] {}".format(gi))
	fm = gi.freqmod_overlay(rinit=0, ginit=0, binit=0)
	fm.map_freq_modulation(omega=omega, phase=phase, lowpass=lowpass)
	fm.save(output_file)
	print("[+] written output image to '{}'".format(output_file))

def process_args():
	""" process the arguments using argparse """
	parser = argparse.ArgumentParser(description=f"CLI for BRImage library {VERSION}\nOnly implements frequency modulation at time of writing.", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('input_image', type=str, nargs=1, help="Input image path; most common formats are accepted.")
	parser.add_argument('--omega', type=float, default=[0.3], nargs=1, help="Frequency omega; controls line spacing. \n - range: 0.0 to 1.0 \n - >1.0 also works, but ugly.")
	parser.add_argument('--phase', type=float, default=[0.5], nargs=1, help="Controls the phase range that is used to map the pixel values into. \n - higher values distort the image more. \n - range: 0.0 to 1.0")
	parser.add_argument('--lowpass', type=float, default=[0], nargs=1, help="Set the lowpass filter amount. \n - lower values blur out fine detail more. \n - set to 0 disables the filter. \n - preconfigured to 30Hz sample rate. \n - range: 0.0 to 1.0.")
	parser.add_argument('-o', '--output_file', nargs=1, type=str, default=["output.jpg"], help="Output image path\n - default 'output.jpg'")

	return parser.parse_args()

def check_file_exists(file):
	""" check file exists; raise exception if not """
	if os.path.isfile(file):
		print(f'[+] input_image path \'{file}\' is okay')
		return
	else:
		raise Exception(f'input_image \'{file}\' does not exist.')

def main():
	""" main cli function """
	print(HEADER)
	args = process_args()
	file = args.input_image[0]
	omega = args.omega[0]
	phase = args.phase[0]
	lowpass = args.lowpass[0]
	output_file = args.output_file[0]

	check_file_exists(file)
	print("[+] starting frequency modulation process...")
	run_fm(file, omega, phase, lowpass, output_file)
	print("[+] done")

if __name__ == '__main__':
	main()