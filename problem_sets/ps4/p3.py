import numpy as np
from library import energy, norm


OFFSET = 10
def V(x) -> float:
    return OFFSET


x = np.linspace(-5, 5, 1000)
y = np.cos(np.pi*x/2)
y = norm(x, y)

print("Calculated energy:", energy(x, y, V))
print("Expected energy:", OFFSET + np.pi**2/4)