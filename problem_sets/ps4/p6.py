import numpy as np
from library import variational, energy, norm
import matplotlib.pyplot as plt

def V(x) -> float:
    """
    Note: This function handles a whole array of x values at once.
    """
    return x ** 2


x = np.linspace(-3, 3, 50)
y = np.zeros_like(x)
y[np.abs(x) < 0.8] = 1

y = norm(x, y)

y1 = variational(x, y, V, 0.1, 10000)
y2 = variational(x, y1, V, 0.01, 10000) 
y3 = variational(x, y2, V, 0.001, 10000)

final_energy = energy(x, y3, V)
delta_e = final_energy - 1
print(f"Difference between expected and calculated ground state energy is {round(delta_e, 5)}")

plt.plot(x, y, label="Initial")
plt.title("Variation Method for Harmonic Oscillator")
plt.plot(x, y1, label="After 10,000 iterations")
plt.plot(x, y2, label="After 20,000 iterations")
plt.plot(x, y3, label="After 30,000 iterations")
plt.legend()
plt.show()