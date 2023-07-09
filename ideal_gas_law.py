from chempy import Substance
from random import randint
import xlsxwriter
import constants

'''Functions'''
def pressure():
    pressure = (randint(900,1100)/10)
    return pressure #returns as kPa

def volume():
    volume = randint(6000, 80000)/10
    return volume #returns as cm3

def moles():
    moles = randint(200, 500)/100
    return moles #returns as mol

def temperature():
    temperature = (randint(2500, 3300)/10)
    return temperature #returns as K

def choose_gas():
    gas = constants.gases[randint(0,len(constants.gases)-1)]
    return gas

'''Question Functions'''
def calculate_pressure(gas):
    V, n, T = volume(), moles(), temperature() #cm3, mol, K
    question = f"{n} moles of {Substance.from_formula(gas).unicode_name} occupies a volume of {V} cm³ at {round(T - 273,1)} °C. Calculate the pressure in kPa to 1 decimal place."
    response = [question, round(((n * constants.gas_constant * T)/(V * 1e-6)/1000),1)]
    unit = "kPa"
    return response, unit

def calculate_volume(gas):
    p, n, T = pressure(), moles(), temperature() #kPa, mol, K
    question = f"{n} moles of {Substance.from_formula(gas).unicode_name} exerts a pressure of {p} kPa at {round(T - 273,1)} °C. Calculate the volume in dm³ to 1 decimal place."
    response = [question, round(((n * constants.gas_constant * T)*1e3/(p*1000)),1)]
    unit = "dm³"
    return response, unit

def calculate_temperature(gas):
    p, V, n = pressure(), volume(), moles()
    question = f"{n} moles of {Substance.from_formula(gas).unicode_name} occupies a volume of {V} cm³ at {p} kPa. Calculate the temperature in °C to 1 decimal place."
    response = [question, round(((p*1000)*(V * 1e-6))/(constants.gas_constant * n),1)]
    unit = "°C"
    return response, unit

def calculate_moles(gas):
    V, p, T = volume(), pressure(), temperature()
    question = f"{Substance.from_formula(gas).unicode_name} occupies a volume of {V} cm³ at {p} kPa and {round(T - 273,1)} °C. Calculate the number of moles in mol to 3 decimal places."
    response = [question, round(((p*1000)*(V*1e-6))/(constants.gas_constant * T),3)]
    unit = "mol"
    return response, unit


'''Recording responses'''

def write_to_excel(option, i):
    if option == 0:
        response, unit = calculate_pressure(choose_gas())
    if option == 1:
        response, unit = calculate_volume(choose_gas())
    if option == 2:
        response, unit = calculate_temperature(choose_gas())
    if option == 3:
        response, unit = calculate_moles(choose_gas())
    worksheet.write(i, 0, f"{i+1}. {response[0]}")
    worksheet.write(i, 1, f"{i+1}. {response[1]} {unit}")

'''Script'''
workbook = xlsxwriter.Workbook("001 Chemistry/Ideal Gas.xlsx")
worksheet = workbook.add_worksheet()
row, col = 0, 0

for i in range(100):
    write_to_excel(1, i)

workbook.close()