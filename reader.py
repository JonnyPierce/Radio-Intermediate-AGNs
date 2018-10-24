import os
import numpy as np

os.chdir('/local/jonnypierce/3C_data/samples')

a,b,c,d,e,f,g,h,i,j = np.loadtxt('Butt_2010.txt', skiprows=1, unpack=True)

print(a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1],j[1])

'''
y=0
z=0
redshift=[]
RA=[]
Dec=[]
FR_class=[]

while(y<len(g)):
    if(t[y]==1 and 16.6>d[y]>7.4 and e[y]>0 and f[y]<0.098):
        z+=1
        RA.append(d[y])
        Dec.append(e[y])
        redshift.append(f[y])
        FR_class.append(u[y])
    y+=1

#np.sort(sort)
x=0
while(x<len(RA)):
    print(RA[x],Dec[x],redshift[x],FR_class[x])
    x+=1
    
print(z)
'''
