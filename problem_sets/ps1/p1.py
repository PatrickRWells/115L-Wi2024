from functools import cache
from fractions import Fraction

"""
Compute the values of the hermite polynomials using the recursion relation
"""

def hermite_polynomial(n):
    """
    Compute the coefficients of the hermite polynomial of degree n.

    The coefficients will be stored as a list of length n+1, 
    """
    start = n % 2 # if n is odd, this returns 1, otherwise 0
    a_n = compute_coefficient(n, start)
    coefficients = [a_n]
    i = start
    while (a_n := compute_coefficient(n, i+2)) != 0:
        coefficients.append(a_n)
        i += 2
    
    normalization = 2**n / coefficients[-1]
    coefficients = [c * normalization for c in coefficients]

    return coefficients

@cache
def compute_coefficient(n: int, m: int) -> Fraction:
    """
    Compute the m-th coefficient of the hermite polynomial of degree n.

    I'm re-indexing the recursion relation here, so we get a_m = C*a_(m-2)
    this becomes:
    
    a_m = [-2(n-m+2)/m(m-1)] a_(m-2)

    the base cases are a_0 = 1 for the even values of n and a_1 = 1 for odd values of n
    For fun, I'm going to use the built-in Fraction object to store the coefficients

    The @cache decorator ensures we never compute the same coefficient twice
    """

    if m in [0, 1]:
        return Fraction(1, 1)

    elif n - m + 2 == 0:
        return 0

    numerator = -2 * (n - m + 2)
    denomenator = m * (m - 1)
    return Fraction(numerator, denomenator) * compute_coefficient(n, m - 2)

def print_polynomial(coefficients: list[Fraction], n: int):
    """
    A bad way to print the polynomial, but it works alright for this case
    """
    polynomial = ""
    for i, c in enumerate(coefficients[::-1]):
        if i != 0:
            if c > 0:
                polynomial += " + "
            else:
                polynomial += " - "
        if i == n:
            polynomial += f"{abs(c)}"
        elif n - 2*i != 0:
            polynomial += f"{abs(c)}u^{n - 2*i}"
        else:
            polynomial += f"{abs(c)}"
    print(polynomial)
    
    


if __name__ == "__main__":
    n = 5
    for i in range(n+1):
        print(f"n = {i}")
        coefficients = hermite_polynomial(i)
        print_polynomial(coefficients, i)
        print("----------------")