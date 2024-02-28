import numpy as np
from typing import Callable

def second_derivative(x: np.ndarray, y: np.ndarray):
    """
    Approximate the second derivative of a function using the central difference
    method. The second derivative is given by:
    d^2y/dx^2 = (y(x+h) - 2y(x) + y(x-h))/h^2

    Note that the first and last points in the array cannot be computed with this method.
    """
    h = x[1] - x[0] # assume uniform spacing

    return (y[2:] - 2*y[1:-1] + y[:-2])/h**2

import matplotlib.pyplot as plt


def norm(x: np.ndarray, y: np.ndarray):
    dx = x[1] - x[0] # assume uniform spacing
    norm = np.sum(y**2)*dx
    return y/np.sqrt(norm)

def energy(x: np.ndarray, y: np.ndarray, V: Callable):
    psi_dp = second_derivative(x, y)
    print(psi_dp)
    h = x[1] - x[0] # assume uniform spacing
    potential = V(x)*y
    print(y)
    print(psi_dp*y[1:-1])
    energy = - psi_dp + potential[1:-1]
    energy = np.sum(energy*y[1:-1]*h)

    return energy 


def V(x) -> float:
    potential = np.zeros_like(x)
    potential[np.abs(x) > 1] = 1000
    return potential

x = np.linspace(-1.2, 1.2, 50)
y_start = np.zeros_like(x)
y_start[np.abs(x) < 0.8] = 1
y = norm(x, y_start)

print(energy(x, y, V))
exit()
dy = 0.1
n_changed = 0
for i in range(10000):
    selection = np.random.randint(1, len(x)-1)
    deltay = np.random.uniform(0, dy)
    y_new = y.copy()
    y_new[selection] += deltay
    y_new = norm(x, y_new)
    if energy(x, y_new, V) < energy(x, y, V):
        n_changed += 1
        y = y_new

print(n_changed)

dy = 0.01
n_changed = 0
for i in range(10000):
    selection = np.random.randint(1, len(x)-1)
    deltay = np.random.uniform(0, dy)
    y_new = y.copy()
    y_new[selection] += deltay
    y_new = norm(x, y_new)
    if energy(x, y_new, V) < energy(x, y, V):
        n_changed += 1
        y = y_new
print(n_changed)

dy = 0.01
n_changed = 0
for i in range(10000):
    selection = np.random.randint(1, len(x)-1)
    deltay = np.random.uniform(0, dy)
    y_new = y.copy()
    y_new[selection] += deltay
    y_new = norm(x, y_new)
    if energy(x, y_new, V) < energy(x, y, V):
        n_changed += 1
        y = y_new
print(n_changed)


theory_y = np.cos(np.pi*x/2)
plt.plot(x, y)
plt.plot(x, theory_y)
plt.show()