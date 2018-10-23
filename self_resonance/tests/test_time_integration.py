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

k = 0.0

x01 = [1.0, 0]
y1 = Pot.integrate(x01, T, k)
print("Integration successful for first initial conditions")

x02 = [0.0, 1.0]
y2 = Pot.integrate(x02, T, k)
print("Integration successful for second initial conditions")

t_plot = np.linspace(0.0, T, 5000)

plt.plot(t_plot, y1[:,0])
plt.savefig('phi_1.png',dpi=150)
plt.close()

plt.plot(t_plot, y2[:,0])
plt.savefig('phi_2.png',dpi=150)
plt.close()
