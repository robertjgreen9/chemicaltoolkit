import chempy as cp
from atomic_numbers import atomic_numbers

molecule = cp.Substance.from_formula("C43H72Cl2P2Ru")
composition = molecule.composition
print(molecule.mass)
masses = []
rel_masses = []
for key, value in composition.items():
    element = atomic_numbers[key - 1][1]
    mass = atomic_numbers[key - 1][2] * value
    masses.append([element, mass])

for i in range(0, len(masses)):
    comp_by_weight = 100 * masses[i][1] / molecule.mass
    rel_masses.append([masses[i][0], comp_by_weight])

s = ''.join(map(str, rel_masses))
print(s)
#print(f"{masses[i][0]}: {'%.3g' % comp_by_weight} %")


print(f"Determine the empirical and molecular formulae of this compound, when the molar mass of the compound has been calculated to be {'%.1f' % molecule.molar_mass()} gmol⁻¹.")