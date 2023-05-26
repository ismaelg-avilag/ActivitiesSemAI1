"""
Proyecto Final
Seminario de Inteligencia Artificial 1

Ismael Guadalupe Avila Guerrero - 215638591
"""

from AG import *
from problem import *

horas_clase_a_la_semana = [1, 5, 2, 6, 4, 8, 7, 3]
creditos = [7, 8, 3, 1, 6, 4, 8, 3]
horas_max_semana = 25

problem = Problem(horas_clase_a_la_semana, creditos, horas_max_semana)
ag = AG(10, 10, 1, 100, 0.1, problem)

ag.run()

