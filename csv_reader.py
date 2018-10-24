import os
import pandas as pd
import numpy as np
import math as m

os.chdir('/local/jonnypierce/3C_data/samples')

data = pd.read_csv('Butt_2010.csv',usecols=[0,1,4,5,8,10],header=0)

name = np.asarray(data['Name'])
redshift = np.asarray(data['redshift'])
spec = np.asarray(data['spec'])
L = np.asarray(data['L_1400'])  # Note - this is the 1.4GHz lum.

name_new = []
redshift_new = []
L_new = []
spec_new = []

x=0

while x<len(redshift):
    if(redshift[x]<0.2):
        redshift_new.append(redshift[x])
    x+=1

y=0

while y<len(L):
    if(m.log10(L[y])<25):
        L_new.append(L[y])
        name_new.append(name[y])
    y+=1

n=0
while n<len(L_new):
    print(name_new[n],L_new[n])
    n+=1
