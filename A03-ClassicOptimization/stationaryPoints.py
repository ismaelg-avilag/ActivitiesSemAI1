"""
Actividad: 3. Encontrar Puntos Estacionarios de Forma Automática
Seminario de Inteligencia Artificial 1
"""

import numpy as np
import matplotlib.pyplot as plt

polynomial = [1, -4, 1, 6]
#polynomial = [6, -12, 5, -2]
#polynomial = [1/3, 8, 63, 7]
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

plt.title('f(x): x³-4x²+x+6')
#plt.title('f(x): 6x³-12x²+5x-2')
#plt.title('f(x): (1/3)x³+8x²+63x+7')
plt.plot(x, y, 'r')
plt.plot(roots, values, '*g')
plt.annotate("Minimo", (roots[0], values[0]))
plt.annotate("Maximo", (roots[1], values[1]))
plt.show()
