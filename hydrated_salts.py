from chempy import Substance
from random import randint, random
import xlsxwriter
from salt_list import salts

file_name = "001 Chemistry\Hydrated salts.xlsx"
water = "H2O"
proper_water = Substance.from_formula(water)
Mr_water = Substance.from_formula(water).mass

def generate_question(i,random_position, row, col):
    name = salts[random_position][0] #formula of random salt
    proper_name = Substance.from_formula(name)
    num_waters = salts[random_position][1] #number of waters of hydration
    Mr_name = Substance.from_formula(name).mass #molar mass of random salt
    random_mass = randint(0,10000) / 1000
    Mr_hydrated = Mr_name + (num_waters * Mr_water)
    moles_hydrated = random_mass / Mr_hydrated
    moles_anhydrous = moles_hydrated
    moles_water = moles_hydrated * num_waters
    mass_anhydrous = moles_anhydrous * Mr_name
    mass_water = moles_water * Mr_water
    question = f"When {'%.3f' % random_mass} g of {proper_name.unicode_name}·x{proper_water.unicode_name} were heated to complete dryness, it was found that {'%.3f' % mass_anhydrous} g of the anhydrous salt, {proper_name.unicode_name}, and {'%.3f' % mass_water} g of water were produced. Deduce the value of x."
    answer = num_waters 
    worksheet.write(row, col, f"{i + 1}. {question}")
    worksheet.write(row, col+1, f"{i + 1}. {answer}")


workbook = xlsxwriter.Workbook(file_name)
worksheet = workbook.add_worksheet()
row, col = 0,0

for i in range(0,500):
    random_position = randint(0,len(salts) - 1)
    generate_question(i, random_position, row, col)
    row += 1

workbook.close()


