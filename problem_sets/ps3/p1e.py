from library import square_well_even, square_well_odd, find_zero, z_to_e
import numpy as np
# P1 E)
# Now, run a test to see if in the limit of large z_0, the allowed energies
# approach the energies of the infinite square well.

z_0 = 500 * np.pi
allowed_z = []
z = 0.01
even = True
while len(allowed_z) < 4:
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
allowed_kinetic = [allowed_e + z_0**2 for allowed_e in allowed_e]
allowed_infinite = [0.25*n**2*np.pi**2 for n in range(1, 5)]
print("P1 D: The allowed kinetic energies for z_0 = 500*pi are: ", allowed_kinetic)
print("The allowed energies of the infiinte square well with width 2a are: ", allowed_infinite)
print("These correspond to the allowed z values: ", allowed_z)