import os, sys

pkg_path = os.path.abspath('..')
sys.path.append(pkg_path)

import potential as pot

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

pot = pot.Potential()

if(pot.phimin() == 0.0):
    print("Test Phimin Okay")
else:
    print("Test phimin Failed")
    #throw TestFail exception

plot_phi = np.linspace(-3.0, 3.0, 10000)

plt.xlabel('$\phi$')
plt.ylabel('$V(\phi)$')
plt.plot(plot_phi, pot.potential(plot_phi), 'r')
plt.savefig('test_phi_plot.png', dpi=150)
plt.close()
