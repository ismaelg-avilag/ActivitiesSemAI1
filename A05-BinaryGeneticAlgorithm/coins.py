"""
Actividad: 5. Algoritmo Genético Binario
Seminario de Inteligencia Artificial 1

Clase Individuo y AG
"""

class Coins:
    def __init__(self, coinsList):
        self._coinsList = coinsList

    def f(self, cromosoma):
        max_sum = 0
        current_sum = 0
        prev_coin_taken = False
        
        for i in range(len(cromosoma)):
            if cromosoma[i] == 1:
                if prev_coin_taken:
                    # Se penaliza la seleccion de monedas adyacentes
                    current_sum = 0
                
                current_sum += self._coinsList[i]
                max_sum = max(max_sum, current_sum)
                prev_coin_taken = True
            
            else:
                prev_coin_taken = False
        
        return max_sum