import numpy.random as random
import numpy as np

def sim2coins(ntests):
# simulate ntests tosses of 2 coins 
    coin1=random.rand(ntests) > 0.5
    coin2=random.rand(ntests) > 0.5
    return np.sum( coin1 == coin2 )/ntests