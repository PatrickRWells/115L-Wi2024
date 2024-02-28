import numpy as np
from library import tise_rk4, find_allowed_energies
from functools import partial
import matplotlib.pyplot as plt

# Problem 3: Find the binding energy of the two square wells with a separation of
# 2*delta. The wells have a width of 2 and a depth of pi**2/4


def V_d(x, delta):
    start = delta
    end = delta + 2

    if abs(x) > start and abs(x) < end:
        return -0.25*np.pi**2
    return 0


def find_binding_energy(delta: float):

    V = partial(V_d, delta=delta)
    max_x = delta + 7

    even_helper = lambda E: tise_rk4(E, 1, 0, 0, max_x, 0.01, V)[1][-1]
    even_energy = find_allowed_energies(even_helper, -0.25*np.pi**2, 0, 1)

    odd_helper = lambda E: tise_rk4(E, 0, 1, 0, max_x, 0.01, V)[1][-1]
    odd_energy = find_allowed_energies(odd_helper, -0.25*np.pi**2, 0, 1)

    binding_energy = even_energy[0] - odd_energy[0]
    return binding_energy

delta = np.arange(0, 3, 0.1)
binding_energies = [find_binding_energy(d) for d in delta]
plt.plot(delta, binding_energies)
plt.title("Binding energy $E_{even} - E_{odd}$ as a function of well separation")
plt.show()