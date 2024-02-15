import numpy as np
from scipy.optimize import bisect
from typing import Callable, Tuple

def F(Y: np.ndarray, x: np.ndarray, E: float, V: Callable) -> np.ndarray:
    """
    Takes in the current value of the wavefunction and its derivative, the current
    value of x, the energy, and the potential. Returns the first and second derivatives
    of the wavefunction at the given value of x.
    """

    psi = Y[0]
    phi = Y[1]
    dpsi_dx = phi
    dphi_dx = (V(x)-E)*psi
    F = np.array([dpsi_dx, dphi_dx], float)
    return F

def tise_euler(E: float, psi0: float, phi0: float, a: float, b: float, h: float, V: Callable) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrate the time independent Schrodinger equation using the Euler method. This 
    function integrates from a to b with a step size of h. It returns the x values and
    the unnormalized wavefunction.

    The argument V is a function that takes in x and returns the potential at x.
    """
    Y = np.array([psi0, phi0], float)
    X   = np.arange(a,b,h, float)
    PSI = np.array([psi0], float)
    for x in X:
        # 1st order Runge-Kutta:
        K1 = h*F(Y,x,E, V)
        Y += K1
        PSI = np.append(PSI,Y[0])
    X = np.append(X,b)
    return X,PSI

def tise_rk4(E: float, psi0: float, phi0: float, a: float, b: float, h: float, V: Callable) -> Tuple[np.ndarray, np.ndarray]:
    """
    Integrate the time independent Schrodinger equation using the fourth order
    Runge-Kutta method. This  function integrates from a to b with a step size of h. 
    It returns the x values and the unnormalized wavefunction.

    The argument V is a function that takes in x and returns the potential at x.

    """
    Y = np.array([psi0, phi0], float)
    X   = np.arange(a,b,h, float)
    PSI = np.array([psi0], float)
    for x in X:
        # 4th order Runge-Kutta:
        K1 = h*F(Y,x,E, V)
        K2 = h*F(Y+0.5*K1,x+0.5*h,E, V) # Here are the new lines
        K3 = h*F(Y+0.5*K2,x+0.5*h,E, V)
        K4 = h*F(Y+K3,x+h,E, V)
        Y += (K1+2*K2+2*K3+K4)/6
        PSI = np.append(PSI,Y[0])
    X = np.append(X,b)
    return X,PSI

def normalize_wfn(x: np.ndarray, psi: np.ndarray) -> np.ndarray:
    """
    Compute and return the normalized wavefunction.
    """
    norm = np.sqrt(np.trapz(psi**2, x))
    return psi / norm

def find_allowed_energies(even_helper: Callable, odd_helper: Callable, n: int = 6, E_width: float = 0.1, x_max: float = 7.0) -> list[float]:
    """
    Find the first n allowed energies for a given potential using bisection.

    We do this by slowly widening the energy window until we find a solution.
    Then, we move the energy window to the right of the solution and slowly
    widen the energy window again until we find the next solution. We repeat
    this process until we have found n solutions.

    even_helper and odd_helper are functions that take in an energy and a maximum
    value of x and return the value of the wavefunction at x_max. For each energy interval
    the even_helper will be called first. If it fails to find a solution, the odd_helper
    will be called. If neither find a solution, we move on to the next energy interval.
    """
    E_left = 0
    E_right = 0
    energies = []
    while len(energies) < n:
        E_right += E_width
        try: # See if there's an even solution in the energy window
            E = bisect(lambda E: even_helper(E, x_max), E_left, E_right)
            E_left = E_right
        except ValueError: # There's no even solution in the energy window, try odd
            try:
                E = bisect(lambda E: odd_helper(E, x_max), E_left, E_right)
                E_left = E_right
            except ValueError:
                continue # This skips the rest of the loop and goes to the next iteration
        #If we get to this point, we know we have found a solution
        energies.append(E)
        E_left = E_right
    return energies