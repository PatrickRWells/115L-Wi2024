from library import tise_rk4, find_allowed_energies
import matplotlib.pyplot as plt
import numpy as np

"""
Problem 4: The Sawtooth potential. I am going to do this whole thing 
in one go. The energies will be printed to the console, and then 
we will plot the wavefuncitons.
"""


def V(x):
    return np.abs(x)

even_helper = lambda E, x_max: tise_rk4(E=E,psi0=1,phi0=0,a=0,b=x_max,h=0.01, V=V)[1][-1]
odd_helper = lambda E, x_max: tise_rk4(E=E,psi0=0,phi0=1,a=0,b=x_max,h=0.01, V=V)[1][-1]



energies = find_allowed_energies(even_helper=even_helper, odd_helper=odd_helper, n = 6, E_width = 0.1, x_max = 7)
print(f"The first 6 allowed energies for the sawtooth potential are {energies}")


fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.flatten()
x_max = 7
for i, E in enumerate(energies):
    if i % 2 == 0:
        x, psi = tise_rk4(E,1,0,0,x_max,0.01, V=V)
        psi = np.append(np.flip(psi),psi)
    else:
        x, psi = tise_rk4(E,0,1,0,x_max,0.01, V=V)
        psi = np.append(np.flip(-psi),psi)

    x = np.append(np.flip(-x),x)
    axs[i].plot(x,psi, label=f"E = {E:.2f}")
    axs[i].set_title(f"n = {i}")
    if i != 0:
        axs[i].axhline(0, c="black", ls="--")

fig.suptitle("First 6 allowed wavefunctions for the sawtooth potential")
plt.show()