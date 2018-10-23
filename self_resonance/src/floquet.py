import sys, os
pkg_path = os.path.abspath('../pkg/')
sys.path.append(pkg_path)

import potential as pot

import numpy as np

Pot = pot.Potential('axion_monodromy')

k = np.linspace(0.01, 2.0, 200)
phimax = np.linspace(0.001, 10.0, 200)

max_FE = np.zeros((len(k), len(phimax)))

for i in range(0, len(k)):
    for j in range(0, len(phimax)):
        max_FE[i,j] = Pot.max_Floquet_exp(k[i], phimax[j])

X = np.meshgrid(k, phimax)

np.save('max_FE.npy', max_FE)
np.save('XY.npy', X)
