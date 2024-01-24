import matplotlib.pyplot as plt
from scipy.special import hermite
import numpy as np

plot_range = np.linspace(-5, 5, 1000)
fig, axs = plt.subplots(2, 2, figsize=(15, 15))

axs = axs.flatten()

for i, ax in enumerate(axs):
    """
    I'm ignoring the constants here. Just plutting H_i(u) * exp(-u^2/2)
    
    """

    hermite_values = hermite(i)(plot_range)
    plot_values = hermite_values*np.exp(-plot_range**2/2)


    ax.plot(plot_range, plot_values)
    ax.set_title(f"H_{i}(u)")
    ax.set_xlabel("u")
    ax.set_ylabel(f"$H_{i}(u)$")

plt.show()