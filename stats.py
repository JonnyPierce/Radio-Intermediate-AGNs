'''
Module of stats-related functions.
NOTE: Use Python 3
'''
import numpy as np
import scipy.stats as st
import scipy.stats.distributions as dist
import pandas as pd

def prop(s,n):
    '''
    Given number of successes and sample size, returns proportion/percentage,
    standard error in proportion/percentage.
    
    Inputs: Number of successes and size of sample
    Outputs: Print statement with proportion/percentage of successes +/- error
    '''
    prop = s/n
    per = prop*100

    prop_err = np.sqrt(prop*(1-prop)/n)     # Standard error in measured proportion
    per_err = prop_err*100                  # ^ as % 

    print(prop,"+/-",prop_err,"\n",per,"+/-",per_err,"%")

def z_test(s1,n1,s2,n2):
    '''
    Compares statistical significance of the difference between
    two proportions. Gives N*sigma value for the difference.
    Test hypothesis, H0: p1 - p2 = 0
    Alternative hypothesis, HA: p1 - p2 =/= 0

    Inputs: No. of successes and sample size for two proportions to be compared
    Outputs: Level of statistical significance of difference in proportions
    '''

    p = (s1+s2)/(n1+n2)     # Proportion if considered as one joint population
    p1 = s1/n1          # Proportion in sample 1
    p2 = s2/n2          # Proportion in sample 2

    z = abs((p1-p2)/np.sqrt(p*(1-p)*((1/n1)+(1/n2))))    # Test statistic for validity of H0

    pnorm = st.norm.cdf(z) - st.norm.cdf(-z)    # Probability of value lying within range p(-z) < p < p(z) - "two-tailed"
    print(pnorm)

    print("Within +/-",z,"sigma, or",pnorm*100,"%")

    #if(pnorm<0.382925):
    #    print("Difference under +/- 0.5 sigma significance")

    #if(0.382925<pnorm<0.682689):
    #    print("Difference between +/- 0.5 and +/- 1 sigma significance")

    #if(0.682689<pnorm<0.954500):
    #    print("Difference between +/- 1 and +/- 2 sigma significance")

    #if(0.954500<pnorm<0.997300):
    #    print("Difference between +/- 2 and +/- 3 sigma significance")
    
    #if(0.997300<pnorm<0.999937):
    #    print("Difference between +/- 3 and +/- 4 sigma significance")

    #if(0.999937<pnorm<0.999999):
    #    print("Difference between +/- 4 and +/- 5 sigma significance")

    #if(pnorm>0.999999):
    #    print("Difference greater than +/- 5 sigma significance")

def pearson(infile,x_name,y_name):
    '''
    Test significance of LINEAR correlations in data.
    Note that higher order correlations are not tested, but this is
    good enough for testing the basic presence/absence of a correlation.

    Inputs: .csv file containing data to be tested, names of x and y column headers in file
    Outputs: Pearson correlation coefficient, value 1 < r < -1. p-value to indicate significance.
    1 = total positive correlation, 0 = no correlation, -1 = total negative correlation.
    '''

    data = pd.read_csv(str(infile), usecols=[0,1],header=0)     # Read in .csv file with data
    x = np.asarray(data[str(x_name)])                           # Generate numpy arrays for x and y data
    y = np.asarray(data[str(y_name)])
    
    x_bar = np.mean(x)              # Calculate means of x and y data
    y_bar = np.mean(y)
    cov = 0
    var_x = 0
    var_y = 0

    for n in range(len(x)):                     
        cov += (x[n]-x_bar)*(y[n]-y_bar)        # Iterative sum to calculate covariance for data
        var_x += (x[n]-x_bar)**2                # Iterative sums for variance of x and y
        var_y += (y[n]-y_bar)**2

    std_x = np.sqrt(var_x)                      # Calculate standard devations for x and y data 
    std_y = np.sqrt(var_y)
    r = cov/(std_x*std_y)                       # Calculate Pearson correlation coefficient

    print("The Pearson correlation coefficient is:",r)

    df = len(x)-2                               # Degrees of freedom for x,y data
    t = abs(r*(df/(1-r**2))**0.5)                    # t-value corresponding to r, df values
    print("The t-value is:",t)

    p_t = 2*(1 - st.t.cdf(t,df,loc=0,scale=1))    # Corresponding p-value to indicate significance of result.
    print("The p-value is:",p_t)

def spearman(infile,x_name,y_name):
    '''
    Test significance of multiple order correlations in data.

    Inputs: .csv file containing data to be tested, names of x and y column headers in file
    Outputs: Spearman's rank correlation coefficient, value 1 < r < -1. p-value to indicate significance.
    1 = total positive correlation, 0 = no correlation, -1 = total negative correlation.
    '''

    data = pd.read_csv(str(infile), usecols=[0,1],header=0)     # Read in .csv file with data
    x = np.asarray(data[str(x_name)])                           # Generate numpy arrays for x and y data
    y = np.asarray(data[str(y_name)])
    
    x_rank = st.rankdata(x)             # Ranking of input data - where Spearman differs from Pearson
    y_rank = st.rankdata(y)

    xr_bar = np.mean(x_rank)              # Calculate means of x and y data
    yr_bar = np.mean(y_rank)
    cov_r = 0
    var_xr = 0
    var_yr = 0

    for n in range(len(x_rank)):                     
        cov_r += (x_rank[n]-xr_bar)*(y_rank[n]-yr_bar)        # Iterative sum to calculate covariance for ranked data
        var_xr += (x_rank[n]-xr_bar)**2                # Iterative sums for variance of ranked x and y data
        var_yr += (y_rank[n]-yr_bar)**2

    std_xr = np.sqrt(var_xr)                      # Calculate standard devations for ranked x and y data 
    std_yr = np.sqrt(var_yr)
    rs = cov_r/(std_xr*std_yr)                       # Calculate Spearman correlation coefficient

    print("The Spearman correlation coefficient is:",rs)

    df = len(x_rank)-2                               # Degrees of freedom for x,y data
    t = abs(rs*(df/(1-rs**2))**0.5)                    # t-value corresponding to rs, df values
    print("The t-value is:",t)

    p_t = 2*(1 - st.t.cdf(t,df,loc=0,scale=1))    # Corresponding p-value to indicate significance of result.
    print("The p-value from the t-test is:",p_t)

    S = (len(x_rank)**3 - len(x_rank))*(1-rs)/6     # S-test statistic corresponding to rs
    print("The S-value is:",S)

    # I’m not exactly sure how the p-value is computed in the cor.test() function, 
    # it’s likely an asymptotic approach due to the sample size. 
    # However, both p-values are so similar it can be agreed the manual calculation 
    # verifies the output. (Aaron Schlegel, rpubs.com)

def prop_beta(c,k,n):
    '''
    Generate upper and lower limits for proportions based on defined confidence level. 
    Based on Bayesian beta distribution rather than assumed normal distribution.

    Inputs: Confidence level required as decimal (c), number of successes (k), sample size (n)
    Outputs: Proportion of successes, as well as lower and upper limits for defined conf. level
    '''

    p_lower = dist.beta.ppf((1-c)/2,k+1,n-k+1)
    p_upper = dist.beta.ppf(1-(1-c)/2,k+1,n-k+1)

    prop = k/n

    #print("The proportion is",str(prop)+",","with lower and upper limits of",p_lower,"and",p_upper,"for a confidence level of",str(c)+".")

    return(p_lower,prop,p_upper)