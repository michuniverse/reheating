import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

max_FE = np.load('max_FE.npy')
phimax, k = np.load('XY.npy')

fig = plt.figure()
plt.xlabel('$k$')
plt.ylabel('$\phi_{max}$')
plt.pcolor(k, phimax, max_FE, vmin=0.0, cmap='plasma')
plt.colorbar()
plt.savefig('Floquet_diagram.png', dpi=200)
plt.close()
