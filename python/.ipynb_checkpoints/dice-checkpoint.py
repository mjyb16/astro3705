import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial,comb

def rolldice(nsims):
# nsims is number of simulations to do
    prob=1/6.
    is_one=(random.rand(int(nsims),100) < prob)
# generate nsims sets of 100 rolls
    ndice_array=np.array([2,5,10,25,100])

    for i,ndice in enumerate(ndice_array):
        plt.figure(i) # create a new figure for each plot
        plt.hist( np.sum(is_one[:,0:ndice],axis=1), range=(-0.5,ndice+0.5),bins=(ndice + 1))#,hold=False)
        x=np.arange(ndice + 1)
        plt.plot(x,nsims*comb(ndice,x)*prob**x*(1-prob)**(ndice-x),'ro')
        plt.title(str(ndice) + ' dice')
        # convert ndice to a string with str(), then use that to title the plot
        plt.xlabel('Total number of ones')
        plt.show()
        print(f'ndice: {ndice}')
        print(f'np.mean: {np.mean(np.sum(is_one[:,0:ndice],axis=1))}')
        print(f'np.sum: {np.sum(np.sum(is_one[:,0:ndice],axis=1))/nsims:.4f}')
        print(f'Expected mean: {ndice*prob:.4f} ')
        print(f'np.std**2:{np.std( np.sum(is_one[:, 0:ndice],axis=1) )**2:.4f}')
        print(f'np.var: {np.var( np.sum(is_one[:, 0:ndice],axis=1) ) :.4f}')
        print(f'Expected variance: {ndice*prob*(1-prob):.4f}')
        print('')