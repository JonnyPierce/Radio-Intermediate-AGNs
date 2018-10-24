import os

if __name__ == "__main__":

    os.chdir("/local/jonnypierce/GALFIT/int_power/J0810/")
    
    x_c = 83.5
    y_c = 44
    r_lim = 12.91291
    x=0
    y=0

    bad_star = open("J0810_bad_star.txt","w")

    for x in range(70,96):
        for y in range(31,57):
            r = ((x-x_c)**2 + (y-y_c)**2)**0.5
            print(r)
            if(r<=r_lim):
                bad_star.write(str(x) + " " + str(y) + "\n")
            
    bad_star.close()
