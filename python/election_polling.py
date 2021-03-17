import numpy as np
import scipy.interpolate as interpol
import scipy.integrate as integrate

def dem_prob_2020(n, m, prange, uniform = False):
    p=np.linspace(0.,1.,501) # evenly-spaced array of probability values
    likelihood=p**m * (1-p)**(n-m) # likelihood function (unnormalized).
    
    previous_prop = 0.4746
    N_prior = previous_prop*(1-previous_prop)*(2/.15)**2
    prior = p**(N_prior*previous_prop) * (1-p)**(N_prior - N_prior*previous_prop)
    if uniform:
        prior = 0*prior + 1
    
    # A reasonable first guess is the uniform prior, since we know the order of magnitude of p (between 0 and 1), and we don't need transformation invariance since we are going to stick with proportions. Also, we can reasonably assume that values of p near 0.5 are at least as likely as values near 0 or 1 (elections in the US are almost never landslides), while the Jeffreys prior (and Haldane) assume that values near 0 or 1 are more likely. However, we also know that Pennsylvania is usually a battleground state, so we should actually choose a distribution that peaks near 0.5 (not uniform). One option is to use the ratio of registered democrats to registered republicans in a binomial prior, but this requires an assumption about the ratio of democratic-leaning to republican-leaning independents (same as ratio of party-affiliated voters) as well as an assumption about turnout, both of which we we cannot draw a conclusion about. A better option, especially since one of the candidates is an incumbent, is to use the proportion from the previous election as a binomial prior, and treat the poll as an "update" to our belief about the system since then. We can weight the previous election lightly to reflect the possibility that voter preferences have changed in the meantime. A calculation of the weight is made by assuming the following consistency condition: in 95% of elections, the proportion of a candidate's votes will be within 0.15 of the previous election's results for the candidate from the same party. This is consistent with previous results in Pennsylvania in the era known as the Sixth Party System (1972-current). Thus, we can assume that 2*sigma = 0.15*N, where N is the effective "sample size" for our prior indicating our degree of belief, and calculate N using the formula for binomial sigma. 
    
    norm, err = integrate.quad(interpol.interp1d(p, likelihood*prior, kind='cubic'), 1e-5,1-1e-5,epsrel=1.e-4)
    posterior = interpol.interp1d(p, likelihood*prior/norm, kind='cubic')
    probability, _ = integrate.quad(posterior, m/n - prange, m/n + prange, epsrel=1.e-4)
    return probability
    
def rep_prob_2020(n, m, prange, uniform = False):
    p=np.linspace(0.,1.,501) # evenly-spaced array of probability values
    likelihood=p**m * (1-p)**(n-m) # likelihood function (unnormalized).
    
    previous_prop = 0.4817
    N_prior = previous_prop*(1-previous_prop)*(2/.15)**2
    prior = p**(N_prior*previous_prop) * (1-p)**(N_prior - N_prior*previous_prop) 
    if uniform:
        prior = 0*prior + 1
    
    norm, err = integrate.quad(interpol.interp1d(p, likelihood*prior, kind='cubic'), 1e-5,1-1e-5,epsrel=1.e-4)
    posterior = interpol.interp1d(p, likelihood*prior/norm, kind='cubic')
    probability, _ = integrate.quad(posterior, m/n - prange, m/n + prange, epsrel=1.e-4)
    return probability