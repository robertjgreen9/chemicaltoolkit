from chempy import Substance, balance_stoichiometry, mass_fractions
from pprint import pprint

reactants = {'C3H6','O2'}
products = {'CO2','H2O'}

reac, prod = balance_stoichiometry(reactants,products)

molecule = 'Fe(CN)6-3'
formula = Substance.from_formula(molecule)
nice = formula.unicode_name
print(nice)