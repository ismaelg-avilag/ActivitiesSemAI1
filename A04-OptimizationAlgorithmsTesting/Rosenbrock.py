"""
Actividad: 4. Funciones para probar algoritmos de optimizacion
Seminario de Inteligencia Artificial 1

- Rosenbrock
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

b = 10
f = lambda x, y: (x-1)**2 + b*(y-x**2)**2;

fig = plt.figure()
ax = fig.gca(projection = '3d')

X = np.arange(-2.048, 2.048, 0.1)
Y = np.arange(-2.048, 2.048, 0.1)

X, Y = np.meshgrid(X, Y)

Z = f(X, Y)

surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 1)
fig.colorbar(surf)
plt.show()