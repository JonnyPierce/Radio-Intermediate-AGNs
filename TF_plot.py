import matplotlib.pyplot as plt
import numpy as np
#f = [37.5,68.75,95]
#d = [0.41,0.28,1.6] # Error bars for x
#e = [0.17,0.64,1.66]

#a =  [23.076,26.6] # Data set 1
#b =  [47,95] # Data set 2

#c = [8.8,2.3] # Error bar values, y
#f = [8.8,2.3]
#d = [0.576,1.6] # Error bars for x
#e = [0.924,1.66]
a_h = [22.5,23.25,24]
b_h = [37.5,68.75,94]
c_h = [0.42,0.28,1.6]
d_h = [0.16,0.64]
e_h = [12,12,3.5]

a = [22.92,23.36]
b = [37.5,68.75]
c = [0.42,0.28]
d = [0.16,0.64]
e = [12,12]
a1 = [27.00]
b1 = [94]
c1 = [1.38]
d1 = [1.26]
e1 = [3.92]

#test = np.array(b)
#plt.scatter(a,b,color='black', marker='.',linewidth=1.0)
#plt.plot(a,b,color='black',alpha=0.5)
plt.scatter(a,b,color='#03a2b6',marker='D',linewidth=0.75,alpha=0.9)
plt.scatter(a1,b1,color='#0030a4',marker='D',linewidth=0.75,alpha=0.75)
#plt.hist(a,bins='auto',histtype='step')
#plt.hist(test, bins=[22.5,23.25,24], histtype='step', rwidth=0.8, linewidth=3.0, fill=False)
'''
plt.plot([0,9.5], [25.49, 25.49], color='red', linestyle='--', linewidth=0.5)
plt.plot([9.5,18.5], [25.17, 25.17], color='red', linestyle='--', linewidth=0.5)
plt.plot([18.5,26.5], [25.55, 25.55], color='red', linestyle='--', linewidth=0.5)
plt.plot([26.5,35.5], [25.53, 25.53], color='red', linestyle='--', linewidth=0.5)
'''

plt.plot([22.519, 23.07], [37.5, 37.5], color='#03a2b6', linestyle=':', linewidth=1)
plt.plot([23.082, 23.98], [68.75, 68.75], color='#03a2b6', linestyle=':', linewidth=1)
plt.plot([25.62, 28.26], [94, 94], color='#0030a4', linestyle=':', linewidth=1)

plt.errorbar(a,b,yerr=e,linestyle="None",color='#03a2b6',linewidth=0.75,capsize=3,alpha=0.9)
plt.errorbar(a1,b1,yerr=e1,linestyle="None",color='#0030a4',linewidth=0.75,capsize=3,alpha=0.75)

# add some text for labels, title and axes ticks
#plt.title('Figure 2')
plt.xlim(22.0,28.5)
plt.ylim(0,100)
plt.ylabel('Clear tidal features (%)',size=13,labelpad=10)
plt.xlabel('log($\mathrm{L_{1.4GHz})}$ [W/Hz]',size=14,labelpad=10)
plt.xticks([22.0, 22.5,23.0,23.5,24.0,24.5,25.0,25.5,26.0,26.5,27.0,27.5,28.0,28.5])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
#plt.axvspan(24.0,25.0,alpha=0.1,color='gray')
#plt.axvspan(9.5,18.5,alpha=0.1,color='blue')
#plt.axvspan(18.5,26.5,alpha=0.1,color='red')
#plt.axvspan(26.5,35.5,alpha=0.1,color='green')
plt.tick_params(axis='both',direction='inout',top='on',right='on', labelsize=12)

#blue_line = mlines.Line2D([], [], color='blue', marker='D', markersize=15, label='Radio-intermediate HERGs')
#blue_line = mlines.Line2D([], [], color='blue', marker='D', markersize=15, label='2 Jy')
#plt.legend(handles=[blue_line])

line_up, = plt.plot(a, color='#03a2b6', marker='D', markersize=6, label='Radio-intermediate HERGs', linestyle=":")
line_down, = plt.plot(a1, color='#0030a4', marker='D', markersize=6, label='2 Jy HERGs', linestyle=":")
plt.legend([line_up, line_down], ['Radio-intermediate HERGs', '2 Jy SLRGs'],loc=4,bbox_to_anchor=(0.98, 0.05),fontsize=13)

plt.show()
