import numpy as np
from scipy.integrate import quadrature, odeint

class Potential:
    def __init__(self):
        #blablabla
        return None

    def V(self, phi):
        return np.sqrt(1.0 + phi**2) - 1.0

    def Vdd(self, phi):
        return 1.0/np.sqrt(1.0+phi**2)**(3)

    def period(self, phimax):
        _phimin = self.phimin()
        f = lambda phi : np.sqrt(2.0/(self.V(phimax)-self.V(phi)))
        T = quadrature(f, _phimin, phimax)
        return T[0]

    def phimin(self):
        return 0.0

    def system_equations(self, x, t, k):
        phi, pi = x

        _vdd = self.Vdd(phi)

        phi_dot = pi
        pi_dot = -(k**2 + _vdd)*phi

        return [phi_dot, pi_dot]

    def integrate(self, x0, T, k, N_steps=5000):
        t = np.linspace(0.0, T, N_steps)
        x = odeint(self.system_equations, x0, t, args=(k,))
        return x
