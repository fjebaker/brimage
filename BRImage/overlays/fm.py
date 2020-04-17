import numpy as np
from scipy.signal import butter, filtfilt, freqz

from BRImage.overlays.glitch import GOverlay
from BRImage.glitchcore import remap
from __brimage_lib.algorithms import freqmod_row

def _butter_lowpass(cutoff, fs, order=5):
	""" calculates the butterworth lowpass filter """
	nyq = 0.5 * fs
	normal_cutoff = cutoff / nyq
	b, a = butter(order, normal_cutoff, btype='low', analog=False)
	return b, a


def _butter_lowpass_filter(data, cutoff, fs, order=5):
	""" applies a butterworth lowpass filter """
	b, a = _butter_lowpass(cutoff, fs, order=order)
	y = filtfilt(b, a, data)
	return y


class FreqModOverlay(GOverlay):
	""" Frequncy Modulation Overlay """
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.min_phase = 0
		self.max_phase = 0

	def map_freq_modulation(self, grayscale=True, lowpass=0, **kwargs):
		""" calculates frequency modulation and imposes it on the return image """
		img = np.array(self._gimage.get_image())
		self.grayscale = grayscale
		self._set_hyper_parameters(**kwargs)

		if grayscale:
			img = np.mean(img, axis=2)
			self._image = self._apply_to(img, lowpass)
		else:
			image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
			for i in range(img.shape[-1]):
				print(f'Processing channel {i}')
				channel = img[:, :, i]
				image[..., i] = self._apply_to(channel, lowpass)
			self._image = image


	def _apply_to(self, channel, lowpass):
		""" applies the FM algorithm to a specific channel """
		new_channel = []
		for row in channel:
			row = freqmod_row(row, self.width, self.max_phase, self.omega)
			if lowpass > 0.000001:	# float comparsison check
				row = self._lowpass(row, lowpass)
			new_channel.append(
				row
			)

		new_channel = np.array(new_channel)
		new_channel = remap(new_channel, np.min(new_channel), np.max(new_channel), 0, 255)
		return np.array(new_channel)

	def _lowpass(self, row, amount):
		""" apply a lowpass filter to the row """
		order = 6
		freq_sample = 30
		cutoff = amount * freq_sample
		return _butter_lowpass_filter(row, cutoff, freq_sample, order)

	def _set_hyper_parameters(self, omega=0.1, phase=0.1, quantization=0, **kwargs):
		""" sets the necessary phase and omega values """
		omega = remap(omega, 0, 1, 
			2 * np.pi / (0.5 * self.width),
			2 * np.pi / (0.005 * self.width)
		)
		phase = remap(phase, 0, 1, 0, 2*np.pi)

		self.omega = omega
		self.max_phase = phase
		self.min_phase = -phase
		self.quantization = quantization

	def post_quantize(self, quant):
		""" apply quantization after the image has been generated """
		image = np.round_(remap(self._image, 0, 255, 0, quant))
		self._image = remap(image, 0, quant, 0, 255)

	def save(self, name, **kwargs):
		if self.grayscale:
			super().save(name, cmap='gray')
		else:
			super().save(name, **kwargs)