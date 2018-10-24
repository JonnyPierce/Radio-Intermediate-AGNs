import astropy.io.fits as pyfits
import os
import numpy as np

def getheader(dataFrame,ext,field):
    #header = pyfits.getheader(dataFrame)
    #target = header['OBJECT']
    hdul = pyfits.open(dataFrame)
    info = hdul[ext].header[field]

    return info

def make_fits(array,filename):
    '''Generates fits file with given name with values from input array'''
    
    hdu = pyfits.PrimaryHDU(array)              # Assigns 'data' array to Primary HDU
    hdu.writeto(filename,clobber=True)    # Generates fits file using 'data' array. Clobber=True overwrites file if it exists.

def read_fits(infile):
    '''Takes input fits file and opens it for reading as an array'''
    
    hdulist = pyfits.open(infile)
    # Note: Have to switch x and y here using .T (transpose) function because scidata array is produced as [y,x].CHECK WHEN USING.
    scidata = hdulist[0].data.T 
    
    return scidata

if __name__ == "__main__":
    
    scidata = (np.zeros((192,283))).T   # Makes array with size 154 x 142, and values zero

    '''Example use: Reading then updating fits file to represent masking of star in S of J0810_s.fits image'''
    
    os.chdir("/local/jonnypierce//backed_up_on_astro3/GALFIT/int_power/J0838/")

    filename = "star_mask.fits"
    #scidata = read_fits(filename)   # Pre-existing fits image made from array of zeroes (as above)

    with open("J0838_bad_star.txt","r") as star:    # Opens file with bad pixel coordinates
        for line in star:
            x = int(line.split()[0])
            y = int(line.split()[1])
            scidata[y,x] = 1
    
    make_fits(scidata,filename)     # Overwrites original file with new fits image made from updated array