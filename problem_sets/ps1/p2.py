import numpy as np
from scipy.special import binom, hermite
import math
"""
Compute the coefficients of the hermite polynomial using the generating function.
In class, we saw how to do this by taking derivatives of the generating function.
Here, I'm going to explicitly expand the generating function using the power series
representation of the exponential function.
"""


def exp_coefficients(n: int, u: float):
    """
    Comptutes the coefficients of the power series expansion of the hermite polynomial
    generating function up to degree n. In this case, we're expanding in z, and working
    with a value of u.

    The generating function is 
    exp(-z^2 + 2uz)

    The general power series expansion is:
    e^x = sum(x^n / n!) from n = 0 to inf

    First, we need to know how many terms we need to compute. 

    for (-z^2 + 2uz)^n the lowest order term will be (2uz)^n, so of order n

    So in order to calculate the coefficients of H_n, we need to expand the lhs to 
    the nth order. This will include a number of throwaway terms, but we can just toss
    them out.
    """
    coefficents = compute_power_series_coefficient(n, u)
    # We know that, for a given value of n, the coefficient of z^n will be equal to
    # H_n(u) / n!
    H_n = coefficents[n] * math.factorial(n)
    return H_n  

def compute_power_series_coefficient(n: int, u: float):
    """
    Computes the coefficients of the nth order term in the power series expansion of the
    generating function of the hermite polynomials.

    The highest order term will be of order z^{2n}. We're going to keep all the
    terms and only throw them unneeded ones out at the end.
    """
    # coefficients of all possible powers of z
    coefficients = np.zeros(2*n + 1)
    # We're expanding the taylor series out to the nth term:
    for taylor_n in range(n+1):
        term_coefficients = np.zeros(2*n + 1)
        # Compute the quantity (-z^2 + 2uz)^taylor_n
        # first, get the binomial coefficients
        binom_coefficients = np.array([binom(taylor_n, k) for k in range(taylor_n+1)])  
        for binom_n in range(taylor_n + 1):
            power = 2 * (taylor_n-binom_n) # the z^2 term
            power += binom_n # the 2uz term
            sign = (-1)**(taylor_n-binom_n)

            coefficient = binom_coefficients[binom_n] * sign * 2**binom_n
            coefficient = coefficient * u**binom_n
            coefficient = coefficient / math.factorial(taylor_n)

            term_coefficients[power] = coefficient
        coefficients += term_coefficients
    return coefficients

if __name__ == "__main__":
    u = 0.7 
    n = 2
    value = exp_coefficients(n, u)
    scipy_value = hermite(n)(u)
    assert np.isclose(value, scipy_value, atol=1e-4)
    print(f"The values match! H_{n}({u})= {scipy_value}")
