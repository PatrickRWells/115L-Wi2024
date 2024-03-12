import numpy as np
from typing import Callable

def second_derivative(x: np.ndarray, y: np.ndarray):
    """
    Approximate the second derivative of a function using the central difference
    method. The second derivative is given by:
    d^2y/dx^2 = (y(x+h) - 2y(x) + y(x-h))/h^2

    Note that the first and last points in the array cannot be computed with this method.
    """
    h = x[1] - x[0] # assume uniform spacing
    result = np.zeros_like(y)
    result[1:-1] = (y[2:] - 2*y[1:-1] + y[:-2])/h**2
    return result


def norm(x: np.ndarray, y: np.ndarray):
    """
    Normalize a given wavefunction. This means that the integral of the square of 
    the wavefunction over the entire range is equal to 1. 
    """
    dx = x[1] - x[0] # assume uniform spacing
    norm = np.sum(y**2)*dx
    return y/np.sqrt(norm)

def energy(x: np.ndarray, y: np.ndarray, V: Callable):
    """
    Comptue the energy of a given wavefucntion, given some potential

    E = <psi|H|psi> = <psi|-d^2/dx^2 + V(x)|psi>
    """
    psi_dp = second_derivative(x, y)
    h = x[1] - x[0] # assume uniform spacing
    potential = V(x)*y
    energy = - psi_dp + potential # Note, this is equal to (-d^2/dx^2 + V(x))|psi>
                                  # We still have to take care of the left hand side
    energy = np.sum(energy*y*h)

    return energy 


def variational(x: np.ndarray, y: np.ndarray, V: Callable, dy: float, n_iter: int) -> np.ndarray:
    """
    Use the variational method to compute a new wavefunction. This function allows you
    to specify the number of iterations and the step size for the random walk.
    """
    y = norm(x, y)
    for _ in range(n_iter):
        selection = np.random.randint(1, len(x)-1)
        deltay = np.random.uniform(-dy, dy)
        y_new = y.copy()
        y_new[selection] += deltay
        y_new = norm(x, y_new)
        if energy(x, y_new, V) < energy(x, y, V):
            y = y_new
    return y
    