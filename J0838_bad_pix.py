import os

if __name__ == "__main__":

    os.chdir("/local/jonnypierce/backed_up_on_astro3/GALFIT/int_power/J0838/")
    
    x_c = 86.0
    y_c = 84.0
    r_lim = 69.6096
    x=0
    y=0

    bad_star = open("J0838_bad_star.txt","w")

    for x in range(16,156):
        for y in range(14,154):
            r = ((x-x_c)**2 + (y-y_c)**2)**0.5
            if(r<=r_lim):
                bad_star.write(str(x) + " " + str(y) + "\n")
            
    bad_star.close()
