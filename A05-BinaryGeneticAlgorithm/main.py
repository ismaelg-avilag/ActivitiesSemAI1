"""
Actividad: 5. Algoritmo Genético Binario
Seminario de Inteligencia Artificial 1

main
"""

from AG import *
from coins import *

coinList = [1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1, 1, 20, 20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2, 5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5, 20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2]

coins = Coins(coinList)
ag = AG(100, 99, 1, 1200, 0.01, coins)

ag.run()