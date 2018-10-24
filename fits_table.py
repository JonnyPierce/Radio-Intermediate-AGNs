from astropy.io import fits


def fitsread(intable):

    hdulist = fits.open(intable)
