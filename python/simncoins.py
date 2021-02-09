import numpy.random as random
import numpy as np

def simncoins(ncoins, nsims):
    "returns number of heads after throwing ncoins, repeated nsims times"
    flips = random.rand(nsims, ncoins)
    heads = flips > 0.5
    return np.sum(heads, axis = 1)