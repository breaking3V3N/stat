import scipy.integrate
import math
from scipy import interpolate
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

def integrand(x,y):
    return 3*x


# want to incorporate bounds in the function additionally the quantile would be good as well
#close but not ther eyet
def Compute_integration():
    #x = np.linspace(0, 200, 300)
    I2 = scipy.integrate.dblquad(lambda x, y:3*x,.25,1,lambda x:0,lambda x: .5)[0]
    return I2
print(Compute_integration())