import pyfits
import os
import glob
from fits_functions import read_fits

if __name__ == "__main__":
    
    root_dir = ('/local/jonnypierce/int_RP_sources/processing/stamps/')
    os.chdir(root_dir)

    afile = glob.glob('*_s.fits')

    for file in afile:
        scidata = read_fits(file)     
        max_x, max_y = scidata.shape
        name = str(file)
        filename = name.split(".")[0] + "_bad.txt"
        bad = open(filename,"w")

        for x in range(max_x):
            for y in range(max_y):
                if(scidata[x,y]>70):
                    xc = (x+1)
                    yc = (y+1)        # Because e.g. scidata[4,1] actually has coordinates x=5, y=2
                    bad.write(str(xc) + " " + str(yc) + "\n")

        bad.close()
