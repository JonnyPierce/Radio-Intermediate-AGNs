import os
import math as m
import numpy as np
import pandas as pd
import csv

def coord_conv(RA,Dec):
    "Converts RA and Dec values from angles to h:m:s and prints"
    RA_new = RA*24/360
    RA_h = int(RA_new)
    RA_m = (RA_new-RA_h)*60
    RA_m_new = int(RA_m)
    RA_s = (RA_m-RA_m_new)*60

    if(Dec<0):
        Dec_m = (int(Dec)-Dec)*60
        Dec_m_new = int(Dec_m)
        Dec_s = (Dec_m-Dec_m_new)*60
        print("%d:%d:%.2f,-%d:%d:%.2f" % (RA_h,RA_m_new,RA_s,Dec,
                                     Dec_m_new,Dec_s))
    else:
        Dec_m = (Dec-int(Dec))*60
        Dec_m_new = int(Dec_m)
        Dec_s = (Dec_m-Dec_m_new)*60
        print("%d:%d:%.2f,%d:%d:%.2f" % (RA_h,RA_m_new,RA_s,Dec,
                                     Dec_m_new,Dec_s))

    return;


os.chdir('/local/jonnypierce/samples')

data = pd.read_csv('BH_RA_Dec.csv', header=0)  # Read in csv file

RA = np.asarray(data['RA'])
Dec = np.asarray(data['Dec'])

x = 0

while x<len(RA):
    coord_conv(RA[x],Dec[x])
    x+=1
