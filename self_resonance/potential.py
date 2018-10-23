import numpy as np
from scipy.integrate import quadrature

class Potential:
    def __init__(self):
        #blablabla
        return None

    def potential(self, phi):
        return np.sqrt(1.0 + phi**2) - 1.0

    def period(self, phimax):
        _phimin = phimin()
        f = lambda phi : np.sqrt(2.0/(potential(phimax)-potential(phi)))
        T = quadrature(f, _phimin, phimax)
        return T

    def phimin(self):
        return 0.0
