"""
Actividad: 3. Encontrar Puntos Estacionarios de Forma Automática
Seminario de Inteligencia Artificial 1
"""

import numpy as np
import matplotlib.pyplot as plt

polynomial = [1, -4, 1, 6]
poly = np.poly1d(polynomial)
first_der = np.polyder(poly, 1)
second_der = np.polyder(poly, 1)
roots = np.roots(first_der)
values = np.polyval(poly, roots)
values2d = np.polyval(second_der, roots)

major = np.max(roots) + 0.5
minior = np.min(roots) - 0.5
x = np.linspace(minior, major, 100)
y = np.polyval(poly, x)


plt.plot(x, y, 'r')
plt.plot(roots, values, '*g')
plt.show()
