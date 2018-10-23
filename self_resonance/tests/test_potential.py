import os, sys

sys.path.append(os.path.abspath('/..'))

import potential as pot

import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=true)
plt.rc('font', family='serif')

if(pot.phimin == 0.0):
    print('Test Phimin Okay')
else:
    #throw TestFail exception

plot_phi = np.linspace(-5.0, 5.0, 10000)

plt.xlabel('$\phi$')
plt.ylabel('$V(\phi)$')
plt.plot(plot_phi, pot.potential(plot_phi), 'r')
plt.savefig('test_phi_plot.png', dpi=150)
plt.close()
