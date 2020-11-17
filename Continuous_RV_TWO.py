import scipy.integrate
import math
from scipy import interpolate
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import sympy as sym

x = sym.symbols("x", real = True)

class continuous_pdf:

    def __init__(self, function: sym.exp, x_bounds: list):
        self.function = function
        self.xlb = x_bounds[0]
        self.xub = x_bounds[1]
        self.expected = self.cts_expected_value()
        self.varaince = self.cts_varaince_value()

    def cts_expected_value(self):
        return sym.integrate(self.function * x,(x,self.xlb,self.xub))


    def cts_varaince_value(self):
        return sym.integrate(self.function * (x - self.expected)**2, (x,self.xlb,self.xub))


a = continuous_pdf(x**2,[0,2])
print(a.cts_expected_value())
print(a.cts_varaince_value())