import numpy as np
from scipy.integrate import quad, odeint

class Potential:
    def __init__(self, name):
        self.name = name
        return None

    def V(self, phi):
        """
        V(phi). Currently there are two options. Quadratic for phi-squared potential and Axion-monodromy potential
        INPUT:
        :phi: Array of field values
        RETURNS:
        The potential value as an array
        """
        if(self.name == 'axion_monodromy'):
            return np.sqrt(1.0 + phi*phi) - 1.0
        elif(self.name == 'quadratic'):
            return 0.5*phi*phi
        else:
            raise ValueError('Requested potential not found')

    def Vd(self, phi):
        """
        V'(phi). Currently there are two options. Quadratic for phi-squared potential and Axion-monodromy potential
        INPUT:
        :phi: Array of field values
        RETURNS:
        The potential value as an array
        """
        if(self.name == 'axion_monodromy'):
            return phi/np.sqrt(1.0+phi*phi)
        elif(self.name == 'quadratic'):
            return phi
        else:
            raise ValueError('Requested potential not found')

    def Vdd(self, phi):
        """
        V''(phi). Currently there are two options. Quadratic for phi-squared potential and Axion-monodromy potential
        INPUT:
        :phi: Array of field values
        RETURNS:
        The potential value as an array
        """
        if(self.name == 'axion_monodromy'):
            return 1.0/(np.sqrt(1.0+phi*phi)**(3))
        elif(self.name == 'quadratic'):
            return np.ones(np.shape(phi))
        else:
            raise ValueError('Requested potential not found')

    def period(self, phimax):
        """
        Calculates the time period of oscillation for different potentials.
        DRAFT REFERENCE:
        Amin review. Eqn (49). Note: different convention with the review for phimin.
        INPUT:
        :phimax: A proxy for the energy.
        RETURNS:
        """
        _phimin = self.phimin()
        f = lambda phi : 2.0*np.sqrt(2.0/(self.V(phimax)-self.V(phi)))
        T = quad(f, _phimin, phimax)
        return T[0]

    def phimin(self):
        """
        Value of phi at which the potential is at the minima
        INPUT:
        None
        RETURNS:
        """
        if(self.name == 'axion_monodromy' or self.name == 'quadratic'):
            return 0.0
        else:
            raise ValueError('Requested potential not found')

    def system_equations(self, x, t, k):
        """
        The system of equations to solve numerically using odeint.
        DRAFT REFERENCE:
        Amin review. Eqn (47)
        INPUT:
        :x: Vector of field and its derivative
        :t: Array of time. Required for it to be in form suitable to use in odeint
        :k: Wavenumber
        RETURNS:
        """
        phi, pi, delta_phi, delta_pi = x

        _vd = self.Vd(phi)
        _vdd = self.Vdd(phi)

        phi_dot = pi
        pi_dot = -_vd
        delta_phi_dot = delta_pi
        delta_pi_dot = -(k**2 + _vdd)*delta_phi

        return [phi_dot, pi_dot, delta_phi_dot, delta_pi_dot]

    def integrate(self, x0, T, k, N_steps=5000):
        """
        Function to integrate the system of equations upto sometime
        DRAFT REFERENCE:
        Amin review. Eqn (47),(50)
        INPUT:
        :x0: Initial vector of field and its derivative
        :T: Float. Time upto which to integrate the equations.
        :k: Wavenumber
        :N_steps: Number of steps of integration. Default is 5000.
        RETURNS:
        """
        t = np.linspace(0.0, T, N_steps)
        x = odeint(self.system_equations, x0, t, args=(k,))
        return x

    def max_Floquet_exp(self, k, phi_max):
        """
        This implements the basic algorithm given in section 3 of Amin review.
        INPUT:
        :k:
        :phi_max:
        RETURNS:
        The Floquet exponent for the given value of phi_max and k.
        """
        T = self.period(phi_max)
        x01 = [phi_max, 0.0, 1.0, 0.0]
        x02 = [phi_max, 0.0, 0.0, 1.0]
        y1 = self.integrate(x01, T, k)
        y2 = self.integrate(x02, T, k)
        A = np.array([[y1[-1,2], y1[-1,3]],[y2[-1,2], y2[-1,3]]])
        Lambda = np.linalg.eigvals(A)
        Floquet_exp = np.log(np.abs(Lambda))/T
        maxFloquet_exp = np.max(Floquet_exp)

        return maxFloquet_exp
