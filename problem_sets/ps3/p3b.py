# problem 3: Two finite wells of width 2 and depth pi/2**2, sepearted by a distance
# 6

# define the potential. We set our origin to be the midpoint between the two wells.
# The potential is zero everywhere except in the two wells, where it is -pi**2
# The two wells are 3->5 and -3->-5
import numpy as np
from library import tise_rk4, normalize_wfn, find_allowed_energies
import matplotlib.pyplot as plt


def V(x):
    if abs(x) > 3 and abs(x) < 5:
        return -0.25*np.pi**2
    return 0

# To find a solution, we will use the same technique we used in assignment 2. We
# integrate out from the center of the well, and look for an energy where it goes
# to zero. Let's integrate out to 7




odd_helper = lambda E: tise_rk4(E, 0, 1, 0, 8, 0.01, V)[1][-1]
odd_energy = find_allowed_energies(odd_helper, V(4), 0, 1)

print(odd_energy)

x_odd, psi_odd = tise_rk4(odd_energy[0], 0, 1, 0, 8, 0.01, V)
x_odd = np.append(np.flip(-x_odd), x_odd)
psi_odd = np.append(-np.flip(psi_odd), psi_odd)
psi_odd = normalize_wfn(x_odd, psi_odd)
plt.axvline(-3, color='black', ls='--')
plt.axvline(3, color='black', ls='--')
plt.axvline(5, color='black', ls='--')
plt.axvline(-5, color='black', ls='--')
plt.axhline(0, color='black', ls='--')
plt.title("First odd eigenstate of the double well separated by 6 units")

plt.plot(x_odd, psi_odd)
plt.show()
