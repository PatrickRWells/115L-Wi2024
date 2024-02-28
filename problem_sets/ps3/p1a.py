# 1a: Find the single allowed bound state of the square well with a depth 
# of z_0 = pi/2. Use the even characteristic function to find the energy.
from library import square_well_even, find_zero, z_to_e
import numpy as np

z_0 = np.pi / 2
z = find_zero(square_well_even, 0.01, z_0, 0.01, args=(z_0,))
E = z_to_e(z, z_0)
print(f"P1 A: The energy of the single bound state is {E:.3f}.")
print(f"P1 A: This corresponds to z = {z:.3f}.")

# 1b: My f_odd equation can be found in the library.py file.