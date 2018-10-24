import pyfits
import sys, re
import glob
import os
from shutil import move
import numpy
import commands
import datetime
import warnings


""" Get info from header"""
def getname(dataFrame):
    workingFrame = 'tmp.fits'
    header = pyfits.getheader(dataFrame)
    target = header['OBJECT']

    return target


if __name__ == '__main__':

    root_dir = '/local/jonnypierce/int_RP_sources/observations/Observing_2018-03/14_03_18'
    save_err = '/local/jonnypierce/int_RP_sources/observations/Observing_2018-03/bad_data'

    os.chdir(root_dir)
    afile = glob.glob('r1*')

    for j in range(len(afile)):
        os.chdir(root_dir)
        filecheck = os.path.isfile(afile[j])
        if filecheck == True:
            target = getname(afile[j])
            if not os.path.exists(root_dir + '/' + target):
                os.makedirs(root_dir + '/' + target)
            s1 = root_dir + '/' + afile[j]
            s2 = root_dir + '/' + target + '/' + afile[j]
            move(s1,s2)