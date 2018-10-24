import matplotlib.pyplot as plt

a =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
      30, 31, 32,33,34,35] # Data set 1
b =  [25.49,25.49,25.48,25.47,25.48,24.99,25.43,25.39,25.50,25.26,25.15,25.35,25.34,25.34,
      25.27,25.29,25.34,25.47,24.88,25.11,25.44,24.98,24.77,25.13,25.44,25.43,25.51,25.48,
      25.49,25.48,25.46,25.45,25.47,25.48,25.43] # Data set 2

c = [0.006,0.007,0.008,0.009,0.009,0.012,0.01,0.01,0.01,0.006,0.01,0.008,0.011,0.009,0.013,
     0.011,0.005,0.003,0.006,0.01,0.009,0.013,0.014,0.007,0.007,0.006,0.01,0.011,0.013,
     0.009,0.011,0.008,0.007,0.005,0.004] # Error bar values, y
#f = [10.8,11.6,2.3]
#d = [0.41,0.28,1.6] # Error bars for x
#e = [0.17,0.64,1.66]

#a =  [23.076,26.6] # Data set 1
#b =  [47,95] # Data set 2

#c = [8.8,2.3] # Error bar values, y
#f = [8.8,2.3]
#d = [0.576,1.6] # Error bars for x
#e = [0.924,1.66]

s1 = [25.5,25.48,25.17,25.55,25.53]
a1 = [0.5,9.25,18.25,26.25,26.75]

plt.scatter(a,b,color='black', marker='.',linewidth=1.0)
plt.plot(a,b,color='black',alpha=0.5)
plt.scatter(a1,s1,color='red',marker='x',linewidth=1.5)
plt.plot([0,9.5], [25.49, 25.49], color='red', linestyle='--', linewidth=0.5)
plt.plot([9.5,18.5], [25.17, 25.17], color='red', linestyle='--', linewidth=0.5)
plt.plot([18.5,26.5], [25.55, 25.55], color='red', linestyle='--', linewidth=0.5)
plt.plot([26.5,35.5], [25.53, 25.53], color='red', linestyle='--', linewidth=0.5)

plt.errorbar(a,b,yerr=c,linestyle="None",color='black',linewidth=1.0,capsize=3)

# add some text for labels, title and axes ticks
#plt.title('Figure 2')
plt.xlim(0,35.5)
plt.ylim(24.5,26.0)
plt.ylabel('ZP',size=13,labelpad=10)
plt.xlabel('No. of observation',size=14,labelpad=10)
#plt.xticks([22.0, 22.5,23.0,23.5,24.0,24.5,25.0,25.5,26.0,26.5,27.0,27.5,28.0, 28.5])
plt.yticks([24.5,25.0,25.5,26.0])
plt.axvspan(0,9.5,alpha=0.1,color='gray')
plt.axvspan(9.5,18.5,alpha=0.1,color='blue')
plt.axvspan(18.5,26.5,alpha=0.1,color='red')
plt.axvspan(26.5,35.5,alpha=0.1,color='green')
plt.tick_params(axis='both',direction='inout',top='on',right='on')

plt.show()
