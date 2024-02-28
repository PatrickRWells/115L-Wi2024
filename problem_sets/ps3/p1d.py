from library import square_well_even, square_well_odd, find_zero, z_to_e
import numpy as np

# 1 d: Find all allowed energies for the square well with a depth of z_0 = 3*pi

z_0 = 3 * np.pi
allowed_z = []
z = 0.01
even = True
while True:
    if z >= z_0:
        break
    try:
        if even:
            z = find_zero(square_well_even, z, z_0, 0.01, args=(z_0,))
        else:
            z = find_zero(square_well_odd, z, z_0, 0.01, args=(z_0,))
        allowed_z.append(z)
        even = not even
    except ValueError:
        break

allowed_e = [z_to_e(z, z_0) for z in allowed_z] 
print("P1 D: The allowed energies are: ", allowed_e)
print("P1 D: The allowed z values are: ", allowed_z)
