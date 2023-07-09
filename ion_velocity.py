from mendeleev import element
from random import randrange
import sigfig

avogadro_constant = 6.022e23


elements = ["Th"]

questions = 1

def element_generator():
    atom = element(elements[randrange(0,len(elements))])
    return atom

def isotope_generator():
    isotopes = []
    for isotope in element_generator().isotopes:
        isotopes.append(isotope.mass_number)
    return isotopes

def distance_generator():
    distance = randrange(1500,1600)/1000
    return distance

def energy_generator():
    kinetic_energy = (randrange(1000,2000)/1000) * 1e-13
    return kinetic_energy

def time_generator():
    time = randrange(1000,9000) * 1e-12
    return time

def random_pair_generator():
    isotopes = isotope_generator()
    random_isotope_number_1 = randrange(0,len(isotopes))
    random_isotope_1 = isotopes[random_isotope_number_1]
    isotopes.remove(isotopes[random_isotope_number_1])
    random_isotope_number_2 = randrange(0, len(isotopes))
    random_isotope_2 = isotopes[random_isotope_number_2]
    isotopes.remove(isotopes[random_isotope_number_2])
    return random_isotope_1, random_isotope_2

def tof_question_generator():
    distance, energy, time, (i1, i2), symbol = distance_generator(), energy_generator(), time_generator(), random_pair_generator(), element_generator().symbol
    print(f"A cation of {symbol}-{i1} travels through a time-of-flight mass spectrometer in {time} seconds. The kinetic energy of {symbol}-{i1} is {energy} J. Calculate the time-of-flight of a cation of {symbol}-{i2}.")
    answer = ((i2/i1)**0.5)*time
    print(f"{sigfig.round(answer, 4)} s")



tof_question_generator()
