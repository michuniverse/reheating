import os, sys

pkg_path = os.path.abspath('../pkg/')
sys.path.append(pkg_path)

import potential as pot

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

pot = pot.Potential('quadratic')

if(pot.phimin() == 0.0):
    print("Test Phimin Okay")
else:
    print("Test phimin Failed")
    #throw TestFail exception

plot_phi = np.linspace(-3.0, 3.0, 10000)

plt.xlabel('$\phi$')
plt.ylabel('$V(\phi)$')
plt.plot(plot_phi, pot.V(plot_phi), 'r')
plt.savefig('test_V_plot.png', dpi=150)
plt.close()

plt.xlabel('$\phi$')
plt.ylabel('$V(\phi)$')
plt.plot(plot_phi, pot.Vdd(plot_phi), 'r')
plt.savefig('test_Vdd_plot.png', dpi=150)
plt.close()
