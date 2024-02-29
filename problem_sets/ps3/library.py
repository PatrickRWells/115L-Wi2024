import numpy as np
from scipy.optimize import bisect
from typing import Callable, Tuple

def square_well_even(z: float, z_0: float) -> float:
    # Return the value of the even characteristic function for a square well
    # with depth z_0 at z. z_0^2 is the depth of the well, and z is related to
    # the energy of the particle by z^2 = z_0^2 - E, where E is the energy in 
    # units of the lowest energy state of the well.

    # Some error checking:
    # z and z_0 must always be greater than zero

    if z < 0 or z_0 < 0:
        raise ValueError("z and z_o must be greater than zero")
    
    radical = z_0**2 / z**2 - 1
    if radical < 0:
        raise ValueError("z must be less than z_0")
    
    return np.sqrt(radical) - np.tan(z)

def square_well_odd(z: float, z_0: float) -> float:
    # Return the value of the odd characteristic function for a square well
    # with depth z_0 at z. z_0^2 is the depth of the well, and z is related to
    # the energy of the particle by z^2 = z_0^2 - E, where E is the energy in 
    # units of the lowest energy state of the well.

    # Some error checking:
    # z and z_0 must always be greater than zero

    if z < 0 or z_0 < 0:
        raise ValueError("z and z_o must be greater than zero")
    
    radical = z_0**2 / z**2 - 1
    if radical < 0:
        raise ValueError("z must be less than z_0")
    
    return np.sqrt(radical) + 1 / np.tan(z)

def find_zero(f: callable, min_val: float, max_val: float, step: float, args: tuple) -> float:
    # Use the bisection method to find the zero of the function f between a and b
    # with the given arguments
    a = min_val
    b = min_val + step
    while b < max_val:
        try:
            return bisect(f, a, b, args=args)
        except ValueError:
            b += step

    raise ValueError("No zero found in the given range")


def z_to_e(z: float, z_0: float) -> float:
    # Convert the characteristic function value z to the energy E, under the assumption
    # That E_0 = 1.0
    return z**2 - z_0**2

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

def normalize_wfn(x: np.ndarray, psi: np.ndarray) -> np.ndarray:
    """
    Compute and return the normalized wavefunction.
    """
    norm = np.sqrt(np.trapz(psi**2, x))
    return psi / norm



def find_allowed_energies(integration_fn: Callable, E_min: float, E_max: float, n: int = 1, E_width: float = 0.1) -> list[float]:
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
    E_left = E_min
    E_right = E_min + E_width
    energies = []
    while len(energies) < n:
        if E_right >= E_max:
            break
        try: # See if there's an even solution in the energy window
            E = bisect(lambda E: integration_fn(E), E_left, E_right)
            energies.append(E)
            E_left = E_right
        except ValueError: # There's no even solution in the energy window, try odd
            E_right += E_width
            continue
        #If we get to this point, we know we have found a solution
        E_right += E_width

    return energies