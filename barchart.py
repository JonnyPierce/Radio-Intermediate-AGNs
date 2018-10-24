import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

N = 2

'''
features = (75,43.75)
#f_err = (21.7,16.5)

unc = (0,12.5)
#unc_err = (0,8.83)

no_features = (25,43.75)
#no_f_err = (12.5,16.5)
'''

features = (11,4)
#f_err = (,28,21.7,33.1)

unc =(0,2)
#unc_err =(12.5,12.5,0,0)

no_features = (5,10)
#no_f_err = (21.650635094611,17.6776695296637,27.9508497187474,12.5)


ind = np.arange(N)  # the x locations for the groups
width = 0.25       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, features, width, color='b',label='Clear features')
rects2 = ax.bar(ind + width, unc, width, color='g',label='Uncertain')
rects3 = ax.bar(ind + width + width, no_features, width, color='r',label='No features')

# add some text for labels, title and axes ticks
ax.set_ylabel('No. of galaxies',size=20)
ax.set_xticks(ind + width)
ax.set_xticklabels(('24.0 < log(P$_{1.4GHz}$) < 23.08','23.08 < log(P$_{1.4GHz}$) < 22.5'))

#ax.legend((rects1[0], rects2[0], rects3[0]), ('Show features', 'Uncertain',
                                              #'No features'))
ax.tick_params(labelsize=20, pad=20)


#plt.legend(bbox_to_anchor=(1.05, 1), loc=4, borderaxespad=0.)

plt.show()

