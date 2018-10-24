import matplotlib.pyplot as plt
import os  
import sys
from math import *
import pandas as pd
import numpy as np

# Change to directory with .csv file inside
os.chdir('/local/jonnypierce/backed_up_on_astro3/int_RP_sources/Figures_and_plots')

# Use pandas to read the file; header=0 means first row is skipped
data = pd.read_csv('SBvsOIII.csv', usecols=[0,1],header=0)
#print(data.columns[0])
# Fill np arrays with data for x and y and errors if necessary
x = np.asarray(data['log(OIII)'])
y = np.asarray(data['SB_av'])
#x_err = np.asarray(data[''])
#y_err = np.asarray(data[''])

plt.scatter(x,y,color='black', marker='x',linewidth=1.0)



plt.xlim(32.7,34.4)
plt.ylim(23.75,27.00)
plt.xlabel(data.columns[0],size=13,labelpad=10)
plt.ylabel(data.columns[1],size=14,labelpad=10)

plt.gca().invert_yaxis()

plt.show()