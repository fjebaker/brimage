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

"""

from PIL import Image
import numpy as np
import scipy.fftpack as fp

## Functions to go from image to frequency-image and back
im2freq = lambda data: fp.rfft(fp.rfft(data, axis=0),
                               axis=1)
freq2im = lambda f: fp.irfft(fp.irfft(f, axis=1),
                             axis=0)

## Read in data file and transform
data = np.array(Image.open('test.png'))

freq = im2freq(data)
back = freq2im(freq)
# Make sure the forward and backward transforms work!
assert(np.allclose(data, back))

## Helper functions to rescale a frequency-image to [0, 255] and save
remmax = lambda x: x/x.max()
remmin = lambda x: x - np.amin(x, axis=(0,1), keepdims=True)
touint8 = lambda x: (remmax(remmin(x))*(256-1e-4)).astype(int)

def arr2im(data, fname):
    out = Image.new('RGB', data.shape[1::-1])
    out.putdata(map(tuple, data.reshape(-1, 3)))
    out.save(fname)

arr2im(touint8(freq), 'freq.png')

"""