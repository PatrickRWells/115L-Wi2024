from library import tise_rk4, normalize_wfn
import matplotlib.pyplot as plt
import numpy as np

def qho_v(x): 
    return x**2

fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs = axs.flatten()
for n in range(4):
    E = 2*n+1
    if n%2 == 0:
        x, psi = tise_rk4(E=E,psi0=1,phi0=0,a=0,b=5,h=0.01, V=qho_v)
        psi = np.append(np.flip(psi), psi)
    else:
        x, psi = tise_rk4(E=E,psi0=0,phi0=1,a=0,b=5,h=0.01, V=qho_v)
        psi = np.append(np.flip(-psi), psi)
    x = np.append(np.flip(-x), x)
    psi = normalize_wfn(x, psi)
    axs[n].plot(x, psi, label=f"n = {n}")
    axs[n].set_title(f"n = {n}")
    axs[n].axhline(c="k")

fig.suptitle("Problem 2 A: The first 4 eigenstates of the quantum harmonic oscillator")
plt.show()
