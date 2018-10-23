import numpy as np
from scipy.integrate import quad, odeint

class Potential:
    def __init__(self, name):
        self.name = name
        return None

    def V(self, phi):
        if(self.name == 'axion_monodromy'):
            return np.sqrt(1.0 + phi**2) - 1.0
        elif(self.name == 'quadratic'):
            return 0.5*phi*phi
        else:
            raise ValueError('Requested potential not found')

    def Vdd(self, phi):
        if(self.name == 'axion_monodromy'):
            return 1.0/np.sqrt(1.0+phi**2)**(3)
        elif(self.name == 'quadratic'):
            return np.ones(np.shape(phi))
        else:
            raise ValueError('Requested potential not found')

    def period(self, phimax):
        _phimin = self.phimin()
        f = lambda phi : 2.0*np.sqrt(2.0/(self.V(phimax)-self.V(phi)))
        T = quad(f, _phimin, phimax)
        return T[0]

    def phimin(self):
        if(self.name == 'axion_monodromy' or self.name == 'quadratic'):
            return 0.0
        else:
            raise ValueError('Requested potential not found')

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

    def max_Floquet_exp(self, k, phi_max):
        T = self.period(phi_max)
        x01 = [1.0, 0.0]
        x02 = [0.0, 1.0]
        y1 = self.integrate(x01, T, k)
        y2 = self.integrate(x02, T, k)
        A = np.array([[y1[-1,0], y1[-1,1]],[y2[-1,0], y2[-1,1]]])
        Lambda = np.linalg.eigvals(A)
        Floquet_exp = np.log(np.abs(Lambda))/T
        maxFloquet_exp = np.max(Floquet_exp)

        return maxFloquet_exp
