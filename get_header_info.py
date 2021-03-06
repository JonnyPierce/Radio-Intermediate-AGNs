import pyfits
import sys, re
import os
import glob
import numpy
import commands
import datetime
import warnings
import csv

""" Get info from header """
def getinfo(dataFrame):
    workingFrame = 'tmp.fits'
    header = pyfits.getheader(dataFrame)
    target = header['OBJECT']
    ZD_1 = header['ZDSTART']
    ZD_2 = header['ZDEND']

    return target,ZD_1,ZD_2

if __name__ == "__main__":

    root_dir = ("/local/jonnypierce/int_RP_sources/processing") # root directory 
    os.chdir(root_dir)
    afolder1 = glob.glob('n*/')  # Make array of night folder names
    #print(afolder1)
    i = 0
    save_dir = "/local/jonnypierce/int_RP_sources/processing/test/"

    # Initialise arrays
    target = []
    ZD_s = []
    ZD_e = []
    
    while(i<len(afolder1)):
        os.chdir(root_dir+'/'+afolder1[i])
        afolder2 = glob.glob("J*/ORIGINALS/")
        #print(afolder2)
        x=0
        while(x<len(afolder2)):
            os.chdir(root_dir+'/'+afolder1[i]+'/'+afolder2[x])
            j=0
            afile = glob.glob("r*")
            #print(afile)
            while(j<len(afile)):
                filecheck = os.path.isfile(afile[j])
                if filecheck==True:
                    try:
                        name,ZD_1,ZD_2 = getinfo(afile[j])
                        target.append(name) 
                        ZD_s.append(ZD_1)
                        ZD_e.append(ZD_2)
                    except:
                        pass
                j+=1
            x+=1            
        #print(len(afolder2))
        i+=1

    #print(target[0],target[1],target[2],target[3])
    #print(ZD_s[0],ZD_s[1],ZD_s[2],ZD_s[3])
    #print(ZD_e[0],ZD_e[1],ZD_e[2],ZD_e[3])
        
    os.chdir(save_dir)
    with open('ZDs.csv','w') as csvfile:
        write = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        write.writerow(['Target','ZD_1','ZD_2'])
        k = 0
        while(k<len(target)):
            write.writerow([target[k],ZD_s[k],ZD_e[k]])
            k+=1
        

