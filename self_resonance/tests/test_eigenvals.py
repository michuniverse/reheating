import sys, os
pkg_path = os.path.abspath('../pkg/')
sys.path.append(pkg_path)

import potential as pot

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

Pot = pot.Potential('quadratic')

phimax = 1.0
T = Pot.period(phimax)
print("The time period for phimax=" + str(phimax) + " is " + str(T) + "\n")

k = 1.0

x01 = [1.0, 0]
y1 = Pot.integrate(x01, T, k)
x02 = [0.0, 1.0]
y2 = Pot.integrate(x02, T, k)

A = np.array([[y1[-1,0], y1[-1,1]],[y2[-1,0], y2[-1,1]]])

Lambda = np.linalg.eigvals(A)

print("The eigenvalues for the current ICs are "+str(Lambda))

Rlambd = np.real(Lambda)

print("The real part of the eigenvalues are" + str(Rlambd[0]) + " and "+ str(Rlambd[1]))

Floquet_exp = np.log(np.abs(Lambda))/T

print("The Floquet exponents are "+ str(Floquet_exp))

maxFloquet_exp = np.max(Floquet_exp)

print("Max Floquet exp is "+str(maxFloquet_exp))
