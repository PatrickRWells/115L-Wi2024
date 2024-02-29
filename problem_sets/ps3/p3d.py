import numpy as np
from library import tise_rk4, find_allowed_energies, normalize_wfn
from functools import partial
import matplotlib.pyplot as plt

# Problem 3d: Compare the first even eigenstate of the double well with delta = 3 and delta = 0.5

def V_d(x, delta):
    start = delta
    end = delta + 2

    if abs(x) > start and abs(x) < end:
        return -0.25*np.pi**2
    return 0


max_x = 10

# Delta = 3 case 
delta = 3
max_x = delta + 7
V = partial(V_d, delta=delta)
even_helper = lambda E: tise_rk4(E, 1, 0, 0, max_x, 0.01, V)[1][-1]
even_energy_3 = find_allowed_energies(even_helper, -0.25*np.pi**2, 0, 1)

# Integrate and normalize
x_3, psi_3 = tise_rk4(even_energy_3[0], 1, 0, 0, max_x, 0.01, V)
x_3 = np.append(np.flip(-x_3), x_3)
psi_3 = np.append(np.flip(psi_3), psi_3)
psi_3 = normalize_wfn(x_3, psi_3)

# delta = 0.5 case
delta = 0.5
V = partial(V_d, delta=delta)
even_helper = lambda E: tise_rk4(E, 1, 0, 0, max_x, 0.01, V)[1][-1]
even_energy_05 = find_allowed_energies(even_helper, -0.25*np.pi**2, 0, 1)


# Integrate and normalize
x_5, psi_5 = tise_rk4(even_energy_05[0], 1, 0, 0, max_x, 0.01, V)
x_5 = np.append(np.flip(-x_5), x_5)
psi_5 = np.append(np.flip(psi_5), psi_5)
psi_5 = normalize_wfn(x_5, psi_5)



fig, axs = plt.subplots(2, figsize=(10, 10))

axs[0].plot(x_3, psi_3, label="delta = 3")
axs[0].axvline(-3, color='black', ls='--')
axs[0].axvline(3, color='black', ls='--')
axs[0].axvline(5, color='black', ls='--')
axs[0].axvline(-5, color='black', ls='--')
axs[0].title.set_text("First even eigenstate of the double well with delta = 3")

axs[1].title.set_text("First even eigenstate of the double well with delta = 0.5")
axs[1].plot(x_5, psi_5, label="delta = 0.5")
axs[1].axvline(-0.5, color='black', ls='--')
axs[1].axvline(0.5, color='black', ls='--')
axs[1].axvline(2.5, color='black', ls='--')
axs[1].axvline(-2.5, color='black', ls='--')
plt.show()