import fits_functions
import os
import glob
import math as m

if __name__ == "__main__":
    
    root_dir = ('/local/jonnypierce/backed_up_on_astro3/GALFIT/int_power/')
    os.chdir(root_dir)

    afolder = glob.glob('J*')
    afile = []
    afile1 = []

    for file in afolder:
        path = root_dir + str(file) + '/' + str(file) +'-galfit.fits'
        name = path.split(file+"/")[-1]
        # Ignore J0810 and J1243, otherwise append afile with path to required folder and afile1 with model filename for each target
        if not name=="J1243-galfit.fits" and not name=="J0810-galfit.fits":
            afile.append(path)
            afile1.append(name)

    n=0

    while n<len(afile):
        os.chdir(afile[n].split(afile1[n])[0])
        
        filename = afile[n].split("-")[0] + "_info.txt"
        info = open(filename,"w")
        
        # Initialise all flux values and ass. errors to 0, then append throughout code as necessary
        F_1 = 0
        F_2 = 0
        F_3 = 0
        F_agn = 0
        F_b = 0
        F_d = 0
        dF_1 = 0
        dF_2 = 0
        dF_3 = 0
        dF_agn = 0
        dF_b = 0
        dF_d = 0

        # Get zeropoint for target observation and write to output file
        zp = fits_functions.getheader(afile1[n],1,'ZP_D')
        dzp = fits_functions.getheader(afile1[n],1,'ZP_D_ERR')
        info.write("ZP: " + str(zp) + " +/- " + str(dzp) + "\n")

        # Get information for first component of model and write to output file
        x_1 = fits_functions.getheader(afile1[n],2,'1_XC')
        y_1 = fits_functions.getheader(afile1[n],2,'1_YC')
        mag_one = fits_functions.getheader(afile1[n],2,'1_MAG')
        mag_1 = float(mag_one.split(" +")[0])
        dmag_1 = float(mag_one.split("- ")[1])
        Re_1 = fits_functions.getheader(afile1[n],2,'1_RE')
        n_1 = fits_functions.getheader(afile1[n],2,'1_N')
        ar_1 = fits_functions.getheader(afile1[n],2,'1_AR')
        pa_1 = fits_functions.getheader(afile1[n],2,'1_PA')
        
        F_1 = 10**((zp-mag_1)/2.5)
        err_1 = m.sqrt((dzp**2)+(dmag_1**2))/2.5
        dF_1 = err_1*F_1*m.log(10)
        
        info.write("\nx_1: " + str(x_1) + "\n")
        info.write("y_1: " + str(y_1) + "\n")
        info.write("Mag_1: " + str(mag_1) + " +/- " + str(dmag_1) + "\n")
        info.write("Re_1: " + str(Re_1) + "\n")
        info.write("n_1: " + str(n_1) + "\n")
        info.write("AR_1: " + str(ar_1) + "\n")
        info.write("PA_1: " + str(pa_1) + "\n")
        info.write("Flux_1: " + str(F_1) + " +/- " + str(dF_1) + "\n")

        # Get information for second component of model and write to output file *IF NECESSARY*
        if fits_functions.getheader(afile1[n],2,'COMP_2')=='sersic':
            x_2 = fits_functions.getheader(afile1[n],2,'2_XC')
            y_2 = fits_functions.getheader(afile1[n],2,'2_YC')
            mag_two = fits_functions.getheader(afile1[n],2,'2_MAG')
            mag_2 = float(mag_two.split(" +")[0])
            dmag_2 = float(mag_two.split("- ")[1])
            Re_2 = fits_functions.getheader(afile1[n],2,'2_RE')
            n_2 = fits_functions.getheader(afile1[n],2,'2_N')
            ar_2 = fits_functions.getheader(afile1[n],2,'2_AR')
            pa_2 = fits_functions.getheader(afile1[n],2,'2_PA')
             
            F_2 = 10**((zp-mag_2)/2.5)
            err_2 = m.sqrt((dzp**2)+(dmag_2**2))/2.5
            dF_2 = err_2*F_2*m.log(10)
            
            info.write("\nx_2: " + str(x_2) + "\n")
            info.write("y_2: " + str(y_2) + "\n")
            info.write("Mag_2: " + str(mag_2) + " +/- " + str(dmag_2) + "\n")
            info.write("Re_2: " + str(Re_2) + "\n")
            info.write("n_2: " + str(n_2) + "\n")
            info.write("AR_2: " + str(ar_2) + "\n")
            info.write("PA_2: " + str(pa_2) + "\n")
            info.write("Flux_2: " + str(F_2) + " +/- " + str(dF_2) + "\n")

            if n_1 > n_2 and ar_1 > ar_2:
                F_b = F_1
                F_d = F_2
                dF_b = dF_1
                dF_d = dF_2

            if n_1 < n_2 and ar_1 < ar_2:
                F_d = F_1
                F_b = F_2
                dF_d = dF_1
                dF_b = dF_2

            # Get info for third component of model and write to output *IF NECESSARY*
            if fits_functions.getheader(afile1[n],2,'COMP_3')=='sersic':
                x_3 = fits_functions.getheader(afile1[n],2,'3_XC')
                y_3 = fits_functions.getheader(afile1[n],2,'3_YC')
                mag_three = fits_functions.getheader(afile1[n],2,'3_MAG')
                mag_3 = float(mag_three.split(" +")[0])
                dmag_3 = float(mag_three.split("- ")[1])
                Re_3 = fits_functions.getheader(afile1[n],2,'3_RE')
                n_3 = fits_functions.getheader(afile1[n],2,'3_N')
                ar_3 = fits_functions.getheader(afile1[n],2,'3_AR')
                pa_3 = fits_functions.getheader(afile1[n],2,'3_PA')
                
                F_3 = 10**((zp-mag_3)/2.5)
                err_3 = m.sqrt((dzp**2)+(dmag_3**2))/2.5
                dF_3 = err_3*F_3*m.log(10)

                info.write("\nx_3: " + str(x_3) + "\n")
                info.write("y_3: " + str(y_3) + "\n")
                info.write("Mag_3: " + str(mag_3) + " +/- " + str(dmag_3) + "\n")
                info.write("Re_3: " + str(Re_3) + "\n")
                info.write("n_3: " + str(n_3) + "\n")
                info.write("AR_3: " + str(ar_3) + "\n")
                info.write("PA_3: " + str(pa_3) + "\n")
                info.write("Flux_3: " + str(F_3) + " +/- " + str(dF_3) + "\n")
                print("3-components: " + afile1[n])
                
                if afile1[n]=='J1147-galfit.fits' or afile1[n]=='J1529-galfit.fits' or afile1[n]=='J1609-galfit.fits':
                    F_d = F_d + F_3
                    dF_d = m.sqrt(dF_d**2 + dF_3**2)

        # Get information for AGN PSFs in second component and write to output file *IF NECESSARY*
        if fits_functions.getheader(afile1[n],2,'COMP_2')=='psf':
            x_p = fits_functions.getheader(afile1[n],2,'2_XC')
            y_p = fits_functions.getheader(afile1[n],2,'2_YC')
            mag_agn = fits_functions.getheader(afile1[n],2,'2_MAG')
            mag_p = float(mag_agn.split(" +")[0])
            dmag_p = float(mag_agn.split("- ")[1])
            
            F_agn = 10**((zp-mag_p)/2.5)
            err_p = m.sqrt((dzp**2)+(dmag_p**2))/2.5
            dF_agn = err_p*F_agn*m.log(10)

            info.write("\nx_agn: " + str(x_p) + "\n")
            info.write("y_agn: " + str(y_p) + "\n")
            info.write("Mag_agn: " + str(mag_p) + " +/- " + str(dmag_p) +"\n")
            info.write("Flux_agn: " + str(F_agn) + " +/- " + str(dF_agn) + "\n")

            # Assign Sersic profile to disk light and AGN PSF to bulge
            F_d = F_1
            F_b = F_agn
            dF_d = dF_1
            dF_b = dF_agn

        # Get information for AGN PSFs in third component and write to output file *IF NECESSARY*
        if fits_functions.getheader(afile1[n],2,'COMP_3')=='psf':
            x_p = fits_functions.getheader(afile1[n],2,'3_XC')
            y_p = fits_functions.getheader(afile1[n],2,'3_YC')
            mag_agn = fits_functions.getheader(afile1[n],2,'3_MAG')
            mag_p = float(mag_agn.split(" +")[0])
            dmag_p = float(mag_agn.split("- ")[1])
            
            F_agn = 10**((zp-mag_p)/2.5)
            err_p = m.sqrt((dzp**2)+(dmag_p**2))/2.5
            dF_agn = err_p*F_agn*m.log(10)

            info.write("\nx_agn: " + str(x_p) + "\n")
            info.write("y_agn: " + str(y_p) + "\n")
            info.write("Mag_agn: " + str(mag_p) + " +/- " + str(dmag_p) +"\n")
            info.write("Flux_agn: " + str(F_agn) + " +/- " + str(dF_agn) + "\n")        

            F_b = F_b + F_agn
            dF_b = m.sqrt(dF_b**2 + dF_agn**2)

        f_t = F_1 + F_2 + F_3 + F_agn
        df_t = m.sqrt(dF_1**2 + dF_2**2 + dF_3**2 + dF_agn**2)
        m_t = -2.5*m.log(f_t,10) + zp
        dlogf = df_t/(f_t*m.log(10))
        dm_t = m.sqrt((2.5*dlogf)**2 + dzp**2)
        info.write("\nFlux_T: " + str(f_t) + " +/- " + str(df_t) + "\n")
        info.write("Mag_T: " + str(m_t)+ " +/- " + str(dm_t) + "\n")

        if F_b > 0 and F_d > 0: 
            bd = F_b/F_d
            err_bd = m.sqrt((dF_b/F_b)**2 + (dF_d/F_d)**2)
            bt = F_b/f_t
            err_bt = m.sqrt((dF_b/F_b)**2 + (df_t/f_t)**2)
            dt = F_d/f_t
            err_dt = m.sqrt((dF_d/F_d)**2 + (df_t/f_t)**2)
            info.write("\nB/D: " + str(bd) + " +/- " + str(err_bd) + "\n")
            info.write("B/T: " + str(bt) + " +/- " + str(err_bt) + "\n")
            info.write("D/T: " + str(dt) + " +/- " + str(err_dt) + "\n")

        n+=1