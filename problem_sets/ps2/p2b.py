from library import tise_rk4 
import matplotlib.pyplot as plt
import numpy as np

def qho_v(x): 
    return x**2

fig, axs = plt.subplots(2, figsize=(10,10))
axs = axs.flatten()
for i in range(2):
    n = i+1
    E = 2*n+1
    if n%2 == 0:
        x, psi = tise_rk4(E=E,psi0=1,phi0=0,a=0,b=10,h=0.01, V=qho_v)
        psi = np.append(np.flip(psi), psi)
    else:
        x, psi = tise_rk4(E=E,psi0=0,phi0=1,a=0,b=10,h=0.01, V=qho_v)
        psi = np.append(np.flip(-psi), psi)
    x = np.append(np.flip(-x), x)
    axs[i].plot(x, psi, label=f"n = {n}")
    axs[i].set_title(f"n = {n}")
    axs[i].axhline(c="k")

fig.suptitle("Problem 2 B: The integration is unstable for large x")
plt.show()
