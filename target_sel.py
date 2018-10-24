import os
import math as m
import numpy as np
import pandas as pd
import csv

os.chdir('/local/jonnypierce/samples')

data = pd.read_csv('B&H12_Vizier_dat.csv', header=0)  # Read in csv file
#print(data)

# Generate numpy arrays for ID, redshift, luminosity distance, radio flux, coordinates
ID = np.asarray(data['ID']) 
z = np.asarray(data['z'])
LD = np.asarray(data['LD'])
R_f = np.asarray(data['R_flux'])
RA_h = np.asarray(data['RA_h'])
RA_m = np.asarray(data['RA_m'])
RA_s = np.asarray(data['RA_s'])
dec_d = np.asarray(data['dec_d'])
dec_m = np.asarray(data['dec_m'])
dec_s = np.asarray(data['dec_s'])

# Initialise arrays for converted radio fluxes, luminosity distances 
R_f_new = []
LD_new = []

for i in R_f:
    i=float(i)
    j = i*10**-29  # Convert flux to W Hz^-1 m^-2
    R_f_new.append(j)

for k in LD:
    k=float(k)
    l = k*3.09*10**22  # Convert LD to m                               
    LD_new.append(l)

# Initialise arrays for radio power, selection of targets and corresponding IDs/coord
power = []
sel = []
ID_new = []
RA_h_new = []
RA_m_new = []
RA_s_new = []
dec_d_new = []
dec_m_new = []
dec_s_new = []

# Spectrum characterised by F_v ~ v^-a, K-correction by F_int = F_obs*(1+z)^(a-1)
a = 0.7
x = a-1
n = 0

# Convert to radio luminosity (WHz^-1), make power selection, get corresponding IDs
while(n<len(R_f_new)):
    L = (4*m.pi*R_f_new[n]*LD_new[n]**2)*(1+z[n])**x
    power.append(L)
    y = m.log10(power[n])
    '''print(ID[n],z[n],m.log10(power[n]))'''
    if(22.5<y<24):
        ID_new.append(ID[n])
        RA_h_new.append(RA_h[n])
        RA_m_new.append(RA_m[n])
        RA_s_new.append(RA_s[n])
        dec_d_new.append(dec_d[n])
        dec_m_new.append(dec_m[n])
        dec_s_new.append(dec_s[n])
        sel.append(L)
    n += 1

# Print target selection
p=0
while(p<len(sel)):
   # print(ID_new[p],sel[p],"{}:{}:{}".format(RA_h_new[p],RA_m_new[p],RA_s_new[p]),"{}:{}:{}".format(dec_d_new[p],dec_m_new[p],dec_s_new[p]))
    p += 1

# Write output to file

with open('Targets_NumRA.csv','w') as csvfile:
    write = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    write.writerow(['ID','Radio power (W/Hz)','log(RP)','RA','Dec'])
    q=0
    while(q<len(sel)):
        #RA = "{}:{}:{}".format(RA_h_new[q],RA_m_new[q],RA_s_new[q])
        #Dec = "{}:{}:{}".format(dec_d_new[q],dec_m_new[q],dec_s_new[q])
        write.writerow([ID_new[q],sel[q],m.log10(sel[q]),RA,Dec])
        q += 1


output = pd.read_csv('Targets.csv', header=0)
print(output)

print(len(sel))

# Append array elements that have single digits, e.g. 7:25:28.48 -> 07:...

RA_sor = np.asarray(output['RA'])
t=0

while(t<len(RA_sor)):
    RA_ = RA_sor[t].split(":")
    if(int(RA_[0])<10):
        RA_[0] = "0{}".format(RA_[0])
    if(int(RA_[1])<10):
        RA_[1] = "0{}".format(RA_[1])
    if(float(RA_[2])<10):
        RA_[2] = "0{}".format(RA_[2])
    RA_sor[t] = "{}:{}:{}".format(RA_[0],RA_[1],RA_[2])
    t += 1

# Order RAs of targets

RA_sor = sorted(RA_sor)

r = 0
'''
while(r<len(RA_sor)):
    print(RA_sor[r])
    r += 1
'''
