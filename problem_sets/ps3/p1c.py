from library import square_well_even, square_well_odd, find_zero, z_to_e
import numpy as np

# 1c: Find one odd and one even bound state of the square well with a depth
# of z_0 = pi

z_0 = np.pi
z_even = find_zero(square_well_even, 0.01, z_0, 0.01, args=(z_0,))

z_odd = find_zero(square_well_odd, z_even, z_0, 0.01, args=(z_0,))

E_even = z_to_e(z_even, z_0)
E_odd = z_to_e(z_odd, z_0)

print(f"P1 C: The energy of the first even bound state is {E_even:.3f}, which corresponds to z = {z_even:.3f}.")
print(f"P1 C: The energy of the first odd bound state is {E_odd:.3f}, which corresponds to z = {z_odd:.3f}.")

