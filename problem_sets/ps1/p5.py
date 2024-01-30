import matplotlib.pyplot as plt
from scipy.special import hermite
import numpy as np

# Plot the first 4 psi functions. I'm going to mostly ignore the constants here.
# This script will first plot the wavefunctions, then the wavefunctions squared after
# the first plot is closed. Normalization is not important for this plot, so I'm going
# to ignore it.


plot_range = np.linspace(-5, 5, 1000)
fig, axs = plt.subplots(2, 2, figsize=(15, 15))

axs = axs.flatten()

for i, ax in enumerate(axs):
    """
    I'm ignoring the constants here. Just plutting H_i(u) * exp(-u^2/2)
    
    """

    hermite_values = hermite(i)(plot_range)
    plot_values = hermite_values*np.exp(-plot_range**2/2)

    ax.set_yticks([0])
    ax.plot(plot_range, plot_values)
    ax.set_title(f"$\Psi_{i}(x)$")
    ax.set_ylabel(f"$\Psi_{i}(x)$")
    fig.suptitle("First 4 Quantum Harmonic Oscillator Wavefunctions")
    ax.set_xlabel("x")

plt.show()

plot_range = np.linspace(-5, 5, 1000)
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
axs = axs.flatten()


for i, ax in enumerate(axs):
    """
    I'm ignoring the constants here. Just plutting |H_i(u) * exp(-u^2/2)|^2
    
    """

    hermite_values = hermite(i)(plot_range)
    psi_values = hermite_values*np.exp(-plot_range**2/2)

    ax.set_yticks([])

    ax.plot(plot_range, psi_values**2)
    ax.set_title(f"|$\Psi_{i}(x)|^2$")
    ax.set_ylabel(f"|$\Psi_{i}(x)|^2$")
    ax.set_xlabel("x")
    fig.suptitle("First 4 Quantum Harmonic Oscillator Wavefunctions Squared")

plt.show()