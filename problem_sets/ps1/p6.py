"""
Problem 6: Numerically show that the psi functions are orthogonal

This means that the integral from negative infinity to infinity of 

psi_n(u) * psi_m(u) * exp(-u^2) du is equal to 0 if n != m and 1 if n == m

I'm going to integrate in u, rather than x. We can think of this as setting
The values of m, omega, and hbar to 1. In this case, the integral of
psi_n(u) * psi_m(u) * exp(-u^2) has a prefactor of 1/sqrt(pi).

"""
import numpy as np
from scipy.special import hermite

def compute_psi(n: int, u_range: np.ndarray) -> np.ndarray:
    """
    Compute the 
    """
    hermite_fn = hermite(n)
    hermite_values = hermite_fn(u_range)
    psi = hermite_values * np.exp(-u_range**2/2)
    # normalize the psi function
    psi = psi / np.sqrt(2**n * np.math.factorial(n))
    return psi

def compute_integral(n: int, m: int, u_range: np.ndarray) -> float:
    psi_n = compute_psi(n, u_range)
    psi_m = compute_psi(m, u_range)

    integrand = psi_n*psi_m
    integral = np.trapz(integrand, u_range)
    return integral



if __name__ == "__main__":

    u_range = np.linspace(-10, 10, 1000)
    for i in range(10):
        for j in range(10):
            integral = compute_integral(i, j, u_range)
            integral = integral / np.sqrt(np.pi)
            if i == j:
                assert np.isclose(integral, 1, atol=1e-4) 
            else:
                assert np.isclose(integral, 0, atol=1e-4)
    # The "assert" statement will crash the program if the condition is not met
    print("All tests passed!")