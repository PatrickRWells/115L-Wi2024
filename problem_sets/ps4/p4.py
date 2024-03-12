import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from library import energy, norm, variational

def V(x: np.ndarray) -> float:
    """
    This function computes the potential energy for the entire range of x at once.
    """
    result = np.zeros_like(x)
    result[np.abs(x) > 1] = 1000
    return result


if __name__ == "__main__":
    x = np.linspace(-1.2, 1.2, 50)
    y_start = np.zeros_like(x)
    y_start[np.abs(x) < 0.8] = 1
    y = norm(x, y_start)

    y1 = variational(x, y, V, 0.1, 10000)
    y2 = variational(x, y1, V, 0.01, 10000)
    y3 = variational(x, y2, V, 0.001, 10000)


    correct_wavefunction = np.cos(np.pi*x/2)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].plot(x, y, label="Initial")
    axs[0].plot(x, y1, label="After 10000 iterations")
    axs[0].plot(x, y2, label="After 20000 iterations")
    axs[0].plot(x, y3, label="After 30000 iterations")
    axs[1].plot(x, y3, label="Variational Method")
    axs[1].plot(x, correct_wavefunction, label="Analytical Solutions")
    axs[0].legend()
    axs[1].legend()
    plt.suptitle("Variational Method for square well")
    uncertainty = energy(x, y2, V) - energy(x, y3, V)
    print("Uncertainty:", uncertainty)
    print(f"Ground state energy estimated to be {energy(x, y3, V)} +/- {uncertainty}")
    plt.show()