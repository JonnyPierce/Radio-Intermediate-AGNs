import glob
import os

os.chdir('/local/jonnypierce/3C_data')
afolder = glob.glob('*')

i=0

while(i<len(afolder)):
    os.chdir('/local/jonnypierce/3C_data'+'/'+afolder[i])
    afile=glob.glob('r*')
    print afolder[i],len(afile)
    i+=1
