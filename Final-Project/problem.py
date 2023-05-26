"""
Proyecto Final
Seminario de Inteligencia Artificial 1

Ismael Guadalupe Avila Guerrero - 215638591
"""

class Problem:
    def __init__(self, horas_clase_a_la_semana, creditos, horas_max_semana):
        self._horas_clase_a_la_semana = horas_clase_a_la_semana
        self._creditos = creditos
        self._horas_max_semana = horas_max_semana

    def f(self, cromosoma):
        f = 0
        sum_horas = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f += self._creditos[i]
                sum_horas += self._horas_clase_a_la_semana[i]
        
        if sum_horas < self._horas_max_semana:
            return f
        else:
            return 0
