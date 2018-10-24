import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

N = 1

'''
features = (75,43.75)
#f_err = (21.7,16.5)

unc = (0,12.5)
#unc_err = (0,8.83)

no_features = (25,43.75)
#no_f_err = (12.5,16.5)
'''

#features = (50,62.5,37.5,87.5)
#f_err = (25,28,21.7,33.1)

#unc =(12.5,12.5,0,0)
#unc_err =(12.5,12.5,0,0)

#no_features = (37.5,25,62.5,12.5)
#no_f_err = (21.650635094611,17.6776695296637,27.9508497187474,12.5)

ellipticals = (5)
sp = (21)
merger = (6)


ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars


# add some text for labels, title and axes ticks
ax.set_ylabel('No. of galaxies')
ax.set_xlabel
ax.set_xticks(ind + width)
#ax.set_xticklabels(('Elliptical', 'Spiral/disk', 'Merger'))

ax.legend((rects1[0], rects2[0], rects3[0]), ('Elliptical', 'Spiral/disk',
                                              'Merger'))
#ax.tick_params(labelsize=9)


plt.show()

