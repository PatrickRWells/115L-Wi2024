from library import second_derivative
import numpy as np
import matplotlib.pyplot as plt

test_x = np.linspace(0, 2*np.pi, 1000)
test_y = np.sin(test_x)

result = second_derivative(test_x, test_y)
plt.plot(test_x, test_y, label="sin(x)")
plt.plot(test_x, result, label = "d^2/dx^2 sin(x)")
plt.axhline(y=0, c='k', linestyle='--')
plt.legend()
plt.show()