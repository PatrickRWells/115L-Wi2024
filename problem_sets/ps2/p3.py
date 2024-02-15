from library import tise_rk4, find_allowed_energies
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect


def V(x):
    return x**2

even_helper = lambda E, x_max: tise_rk4(E=E,psi0=1,phi0=0,a=0,b=x_max,h=0.01, V=V)[1][-1]
odd_helper = lambda E, x_max: tise_rk4(E=E,psi0=0,phi0=1,a=0,b=x_max,h=0.01, V=V)[1][-1]

energies = find_allowed_energies(even_helper=even_helper, odd_helper=odd_helper, n = 6, E_width = 0.1, x_max = 7)
energies = [round(e, 2) for e in energies]
print(f"The first 6 allowed energies for the quantum harmonic oscillator are {energies}")
