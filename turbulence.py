import pandas as pd
import math
import numpy as np


surfaceArea=0.0505

flow=0.035
rho=1000
diameter=0.254
viscdy=0.001
radius=0.5*diameter
V=flow/(3.14*(radius*radius))

TLEN=0.038*diameter
reynolds=diameter*V*rho/viscdy
tintensity=0.16*(reynolds)**(-1.0/8.0)
nut=V*tintensity*(3.0/2.0)**(0.5)

k=(3.0/2.0)*(0.69*tintensity)**2
epsilon=0.09*(k**(3.0/2.0))/TLEN

print "TLEN is %1.8f" %TLEN
print "Turbulent viscosity is %1.8f" %nut
print "Turbulent intensity is %1.8f" %tintensity
print "Reynolds number is %d" %reynolds
print "k is %1.8f" %k
print "epsilon is %1.8f" %epsilon

