"""
Segundo Examen Parcial
Seminario de Inteligencia Artificial 1 - D03

Ismael Guadalupe Avila Guerrero - 215638591
"""

from AG import *
from problem import *

objects = [13, 8, 25, 4, 18, 6, 33, 22, 45, 11, 76, 10, 1]

problem = Problem(objects, 211)
ag = AG(13, 13, 1, 200, 0.1, problem)

ag.run()
