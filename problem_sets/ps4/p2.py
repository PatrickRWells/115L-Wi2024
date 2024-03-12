from library import norm
import numpy as np


x = np.linspace(-10, 10, 100)
y = np.random.uniform(size = len(x))
y = norm(x, y)
print(np.sum(y**2)*(x[1]-x[0]))