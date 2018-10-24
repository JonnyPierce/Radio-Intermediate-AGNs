import matplotlib.pyplot as plt
import numpy as np

a = [33.28,33.89]
b = [43.75,62.5]
c = [0.294,0.315]
d = [0.417,0.358]
e = [12,12]
a1 = [35.21]
b1 = [94]
c1 = [1.57]
d1 = [1.52]
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

plt.plot([32.86, 33.57], [43.75, 43.75], color='#03a2b6', linestyle=':', linewidth=1)
plt.plot([33.57, 34.24], [62.5, 62.5], color='#03a2b6', linestyle=':', linewidth=1)
plt.plot([33.64, 36.73], [94, 94], color='#0030a4', linestyle=':', linewidth=1)

plt.errorbar(a,b,yerr=e,linestyle="None",color='#03a2b6',linewidth=0.75,capsize=3,alpha=0.9)
plt.errorbar(a1,b1,yerr=e1,linestyle="None",color='#0030a4',linewidth=0.75,capsize=3,alpha=0.75)

# add some text for labels, title and axes ticks
#plt.title('Figure 2')
plt.xlim(32.5,37.0)
plt.ylim(0,100)
plt.ylabel('Clear tidal features (%)',size=13,labelpad=10)
plt.xlabel('log$(\mathrm{L_{[OIII]}}$) [W]',size=14,labelpad=10)
plt.xticks([32.5,33.0,33.5,34.0,34.5,35.0,35.5,36.0,36.5,37.0])
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
line_down, = plt.plot(a1, color='#0030a4', marker='D', markersize=6, label='2 Jy HERGs',linestyle=":")
plt.legend([line_up, line_down], ['Radio-intermediate HERGs', '2 Jy SLRGs'],loc=4,bbox_to_anchor=(0.98, 0.05),fontsize=13)

plt.show()