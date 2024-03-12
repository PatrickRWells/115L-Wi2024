import numpy as np
from library import variational, energy
import matplotlib.pyplot as plt

def V(x) -> float:
    B = 1000
    result = -np.cos(np.pi*x/2)
    result[np.abs(x) > 1] = B
    return result

# Let's try the same thing we did in problem 4

x = np.linspace(-1.2, 1.2, 50)
y = np.zeros_like(x)
y[np.abs(x) < 0.8] = 1

y1 = variational(x, y, V, 0.1, 10000)
y2 = variational(x, y1, V, 0.01, 10000)
y3 = variational(x, y2, V, 0.001, 10000)


plt.plot(x, y, label="Initial")
plt.plot(x, y1, label="After 10,000 iterations")
plt.plot(x, y2, label="After 20,000 iterations")
plt.plot(x, y3, label="After 30,000 iterations")
plt.legend()
plt.title("Variational method for curved well")

final_energy = energy(x, y3, V)
delta_e = final_energy - np.pi**2/4
print(delta_e)
print(f"Expected delta E: {8/(3*np.pi)}")
print(f"Delta E from variational method:", energy(x, y3, V))
plt.show()