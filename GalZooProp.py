import stats as s
import pandas as pd
import numpy as np

c = eval(input("Enter the required confidence level as a decimal: "))

data = pd.read_csv("/local/jonnypierce/backed_up_on_astro3/int_RP_sources/extra_data/galaxy_zoo/morph_prop_deb.csv",header=0)

early = np.asarray(data['k_e'])
late = np.asarray(data['k_sp'])
N = np.asarray(data['n'])

#results = open("morph_prop_"+str(c).split[1](".")+".txt","w")

i,x,y,z=0,0,0,0
while(i<len(early)):
    #results.write(str(i)+"Early-type:"+s.prop_beta(c,early[i],N[i]))
    #print(str(i+1)+") Early-type:")
    p_le,prop_e,p_ue = s.prop_beta(c,early[i],N[i])
    p_ls,prop_s,p_us = s.prop_beta(c,late[i],N[i])

    if(prop_e>prop_s and p_le>p_us):
        print("Early-type -",p_us,p_le)
        x+=1

    elif(prop_e<prop_s and p_ls>p_ue):
        print("Late-type -",p_ue,p_ls)
        y+=1

    else:
        print("Unclear")
        z+=1

    i+=1

#print("Early:",x,str(100*x/32),"\nLate:",y,str(100*y/32),"\nUnclear:",z,str(100*z/32))     # For non-debiased
print("Early:",x,str(100*x/30),"\nLate:",y,str(100*y/30),"\nUnclear:",z,str(100*z/30))      # For debiased as 2 unavailable
