import numpy
np=numpy
import numpy.random as random

def hlmean(data,nsamp=-1):
    # PURPOSE:
    #
    #  Calculate Hodges-Lehmann estimator of mean, using nsamp
    #   bootstraps from the data
    #
    # The Hodges-Lehmann estimator is, formally, the median value of
    #  (x_i+x_j)/2 over all pairs of indices i,j .
    # Here, we estimate that quantity using nsamp randomly chosen values
    # of i & j, rather than using all possible values.
    #
    # Although it has much of the robustness of an ordinary median, the
    # H-L estimator yields much smaller errors (equivalent to the mean of
    # >96% as much data, while the median has errors equivalent to the
    # standard error of 64% as much data).
    #
    # CALLING SEQUENCE:
    #
    #  result=hlmean(data [,nsamp=nsamp])
    #
    # INPUTS:
    #
    #  data: array of values to calculate the H-L mean of
    #
    # OPTIONAL KEYWORD PARAMETERS:
    #
    #  nsamp= : if set, hlmean will use this number of bootstrap
    #  samples to do the calculation.  If not set, it will use a number of random pairs equal to
    #  50 times the number of elements of the data array
    #
    # OUTPUTS:
    #
    #  result: sampling-derived estimate of the H-L mean estimator
    #
    # EXAMPLE:
    #    test=[1,2,0,1,2,20.]
    #    print hlmean(test)
    
    ndata=len(data)
    
    # if the number of samples has not been provided, set it to 50*the size of the data array
    
    if nsamp < 0:
        nsamp=50.*ndata
    nsamp=int(nsamp)

# create resampled version of original data
    newdata = np.random.choice(data,size=(nsamp,2))
    
    # average x1 + x2 from each random draw
    mn = (newdata[:,0]+newdata[:,1])/2.
    
    # calculate the median of the averages
    return(np.median(mn))
