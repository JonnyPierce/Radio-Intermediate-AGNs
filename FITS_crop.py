from astropy.io import fits
from astropy import wcs
from astropy.nddata import Cutout2D
import matplotlib.pyplot as plt

f = fits.open('J0725.fits')
w = wcs.WCS(f[0].header)

newf = fits.PrimaryHDU()
newf.data = f[0].data[100:-100,100:-100]
newf.header = f[0].header
newf.header.update(w[100:-100,100:-100].to_header())

position = (2093,3187)
shape = (300,300)
cutout = Cutout2D(f[0].data,position,shape,wcs=w)

plt.imshow(cutout.data, origin='lower')
