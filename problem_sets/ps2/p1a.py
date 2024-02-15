from library import tise_euler
import matplotlib.pyplot as plt
import numpy as np

def V(x):
    return 0

fig, axs = plt.subplots(2, 2, figsize=(10,10))
ns = [1, 0.7, 1.3]
axs = axs.flatten()

for i, n in enumerate(ns):
    X,PSI = tise_euler(E=n**2*np.pi**2,psi0=1,phi0=0,a=0,b=0.5,h=0.01, V=V)
    axs[i].plot(X,PSI)
    # label
    axs[i].set_title(f"n = {n}")
    axs[i].axhline(c="k")
    axs[i].set_ylim(-1.5,1.5)
    axs[i].axvline(x=0.5, c="k")
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("psi(x)")

fig.suptitle("Problem 1 A: Demonstrating 0.7 and 1.3 are not eigenstates")
plt.show()