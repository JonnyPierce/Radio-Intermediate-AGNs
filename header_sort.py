import pyfits
import sys, re
import os
import glob
from shutil import copyfile
import numpy
import commands
import datetime
import warnings


""" Get info from header """
def getname(dataFrame):
    workingFrame = 'tmp.fits'
    header = pyfits.getheader(dataFrame)
    target = header['OBJECT']

    return target


if __name__ == "__main__":

    root_dir = ("/local/jonnypierce/int_RP_sources/observations/Observing_2018-03/11_03_18") # root directory 
    os.chdir(root_dir)
    #afolder = glob.glob('20*/raw')
    
    #i = 0
    save_dir = "/local/jonnypierce/int_RP_sources/observations/Observing_2018-03/11_03_18"
    save_err = "/local/jonnypierce/int_RP_sources/observations/Observing_2018-03/bad_data"

    os.chdir(root_dir)
    j=0
    afile = glob.glob("r*")
    while(j<len(afile)):
        os.chdir(root_dir)
        filecheck = os.path.isfile(afile[j])
        if filecheck==True:
            try:
                target = getname(afile[j])
                if not os.path.exists(root_dir+'/'+target):
                    os.makedirs(root_dir+'/'+target)
            s1 = root_dir + '/' + afile[j]
            s2 = root_dir + '/' + target + '/' + afile[j]
            copyfile(s1,s2)
        j+=1
        #else:
         #   pass
        #j+=1

'''    
    while(i<len(afolder)):
        os.chdir(root_dir+'/'+afolder[i])
        j=0
        afile = glob.glob("r*")
        while(j<len(afile)):
            os.chdir(root_dir)
            filecheck = os.path.isfile(afolder[i] + '/' + afile[j])
            if filecheck==True:
                try:
                    target = getname(afolder[i] + '/' + afile[j])
                    if not os.path.exists(root_dir+'/'+target):
                        os.makedirs(root_dir+'/'+target)
                    copyfile(root_dir+'/'+afolder[i]+'/'+afile[j],root_dir+'/'+target+'/'+afile[j])
                except KeyError:
                    copyfile(root_dir+'/'+afolder[i]+'/'+afile[j],save_err+'/'+afile[j])
            else:
                pass
            j+=1
        i+=1
'''
