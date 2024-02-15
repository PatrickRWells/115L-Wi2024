from library import tise_euler, tise_rk4
import matplotlib.pyplot as plt
import numpy as np


def V(x):
    return 0

n = 5
psi_0 = 1
phi_0 = 0
x_rk1, psi_rk1 = tise_euler(E=n**2*np.pi**2,psi0=psi_0, phi0=psi_0, a=0,b=0.5,h=0.01, V=V)
x_rk4, psi_rk4 = tise_rk4(E=n**2*np.pi**2,psi0=psi_0, phi0=psi_0, a=0,b=0.5,h=0.01, V=V)
plt.plot(x_rk1, psi_rk1, label="RK1")
plt.plot(x_rk4, psi_rk4, label="RK4")
# label
plt.title(f"Problem 1 C: Comparing Euler and RK4 for n = {n}")
plt.axhline(c="k")
plt.axvline(x=0.5, c="k")
plt.xlabel("x")
plt.legend()
plt.show()