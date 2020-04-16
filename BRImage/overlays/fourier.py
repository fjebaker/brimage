import scipy.fftpack as FFT 
import numpy as np 

from BRImage.overlays.glitch import GOverlay

class FourierOverlay(GOverlay):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self._freq = None

	def calc_fourier_space(self):
		img = np.array(self._gimage.get_image())
		self._freq = FFT.rfft(FFT.rfft(img, axis=0), axis=1)

	def _sort_image(self):
		freqs = list(set(self._freq.copy().flatten()))
		freqs.sort()
		return freqs

	def use_nth_maxima(self, n):
		freqs = self._sort_image()
		self._freq = np.where(self._freq > freqs[-n], self._freq, 0)

	def use_nth_minima(self, n):
		freqs = self._sort_image()
		self._freq = np.where(self._freq < freqs[n], self._freq, 0)

	def restore_image(self):
		if self._freq is None:
			raise Exception("Forward fft not done.")

		image = FFT.irfft(FFT.irfft(self._freq, axis=1), axis=0)

		remmax = lambda x: x/x.max()
		remmin = lambda x: x - np.amin(x, axis=(0,1), keepdims=True)
		touint8 = lambda x: (remmax(remmin(x))*(256-1e-4)).astype(int)

		self._image = touint8(image)