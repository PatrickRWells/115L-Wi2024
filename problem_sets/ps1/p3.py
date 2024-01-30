from scipy.special import hermite
from functools import cache
import numpy as np

"""
Computee the hermite polynomial using the recursion relation between the polynomials.
"""

def hermite_polynomial(n):
    """
    Computing the coefficients of the hermite polynomial of degree n with the
    recursion relation:

    H_{n+1} = 2u*H_n - 2n*H_{n-1}
    
    """

    coefficients = [0] * (n+1)
    coefficients[0] = 1
    if n > 0:
        coefficients[1] = 2

    for i in range(2, n+1):
        coefficients[i] = 2 * coefficients[i-1] - 2 * (i-1) * coefficients[i-2]

    return coefficients

@cache
def compute_coefficients(n: int):
    """
    I'm re-indexing the recursion relation here, so we get:
    
    H_n = 2u*H_{n-1} - 2(n-1)H_{n-2}'


    """

    if n == 0:
        return np.array([1])
    elif n == 1:
        return np.array([0, 2])
    
    coefficients = np.zeros(n+1)

    nm1 = compute_coefficients(n-1)
    nm2 = compute_coefficients(n-2)


    coefficients[1:] += 2 * nm1
    coefficients[:len(nm2)] -= 2 * (n-1) * nm2


    # Normalize the coefficients
    normalization = 2**n / coefficients[-1]
    coefficients *= normalization
    return coefficients


def compute_hermite_polynomial(n: int, u: float):
    coefficients = compute_coefficients(n)
    value = 0.0
    for i, c in enumerate(coefficients[::-1]):
        value += c * u**(n - i)
    return value

if __name__ == "__main__":
    """
    lets do a test by comparing to scipy's implementation. We'll check to 4 decimal places
    """
    n_tests = 1000

    for n in range(n_tests):
        # pick a random degree between 0 and 10
        n = np.random.randint(10)
        # pick a random value of u between -5 and 5
        u = np.random.uniform(-5, 5)
        # compute the value of the polynomial
        my_value = compute_hermite_polynomial(n, u)
        scipy_value = hermite(n)(u)
        # check if the values are the same. This line will crash the program if they
        # are too far apart
        assert np.isclose(my_value, scipy_value, atol=1e-4)

    print("All tests passed!")


