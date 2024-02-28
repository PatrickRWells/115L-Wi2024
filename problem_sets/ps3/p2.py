import numpy as np
from library import square_well_even, square_well_odd, find_zero, z_to_e, tise_rk4, normalize_wfn
import matplotlib.pyplot as plt
# Problem 2: Plot the two allowed wavefunctions for the square well with a depth of z_0 = pi

def V(x):
    if abs(x) < 1.0:
        return -np.pi**2
    return 0

z_0 = np.pi
z_even = find_zero(square_well_even, 0.01, z_0, 0.01, args=(z_0,))
z_odd = find_zero(square_well_odd, z_even, z_0, 0.01, args=(z_0,))


E_even = z_to_e(z_even, z_0)
E_odd = z_to_e(z_odd, z_0)

x_even, psi_even = tise_rk4(E_even, 1, 0, 0.0, 2, 0.01, V)
x_odd, psi_odd = tise_rk4(E_odd, 0, 1, 0.0, 2, 0.01, V)

# reflect the wavefunctions over the y-axis
psi_even = np.concatenate((np.flip(psi_even), psi_even))
x_even = np.concatenate((-np.flip(x_even), x_even))

psi_odd = np.concatenate((-np.flip(psi_odd), psi_odd))
x_odd = np.concatenate((-np.flip(x_odd), x_odd))

psi_even = normalize_wfn(x_even, psi_even)
psi_odd = normalize_wfn(x_odd, psi_odd)


plt.axhline(0, color='black', ls='--')
plt.axvline(-1, ymin = 0, ymax = 1, color='black', ls='--')
plt.axvline(1, ymin = 0, ymax = 1, color='black', ls='--')
plt.plot(x_even, psi_even, label=f"E = {E_even:.2f}")
plt.plot(x_odd, psi_odd, label=f"E = {E_odd:.2f}")
plt.title("Eigenstates of the square well with a depth of $\pi^2$")
plt.show()