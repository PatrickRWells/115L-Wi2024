from library import tise_rk4, normalize_wfn
import matplotlib.pyplot as plt
import numpy as np


def V(x):
    return 0
for i in range(1, 7):
    if i%2 == 0: # the "odd" solutions
        x, psi = tise_rk4(E=i**2*np.pi**2,psi0=0,phi0=1,a=0,b=0.5,h=0.01, V=V)
        psi = np.append(np.flip(-psi), psi)
    else: # the "even" solutions
        x, psi = tise_rk4(E=i**2*np.pi**2,psi0=1,phi0=0,a=0,b=0.5,h=0.01, V=V)
        psi = np.append(np.flip(psi), psi)    
    # normalize
    x = np.append(np.flip(-x), x)
    psi = normalize_wfn(x, psi)
    # plot
    plt.plot(x, psi, label=f"n = {i}")
# label
plt.title("Problem 1 D: The first 6 eigenstates of the infinite square well")
plt.axhline(c="k")
plt.legend()
plt.show()