"""
Segundo Examen Parcial
Seminario de Inteligencia Artificial 1 - D03

Ismael Guadalupe Avila Guerrero - 215638591
"""

class Problem:
    def __init__(self, valores, limite):
        self._valores = valores
        self._limite = limite

    def f(self, cromosoma):
        f = 0
        suma = 0
        
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f += self._valores[i]
                suma += self._valores[i]
        
        if suma <= self._limite:
            return f
        else:
            return 0
