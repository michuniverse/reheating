import sys, os
pkg_path = os.path.abspath('../pkg/')
sys.path.append(pkg_path)

import potential as pot

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

Pot = pot.Potential()

k = 1.0
phimax = 1.0

max_FE = Pot.max_Floquest_exp(k, phimax)

print("The max Floquet exp for the current ICs is "+str(max_FE))
