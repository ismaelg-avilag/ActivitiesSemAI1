"""
Actividad: 4. Funciones para probar algoritmos de optimizacion
Seminario de Inteligencia Artificial 1

- Sphere
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection = '3d')

X = np.arange(-5.12, 5.12, 0.1)
Y = np.arange(-5.12, 5.12, 0.1)

X, Y = np.meshgrid(X, Y)

Z = X**2 + Y**2

surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 1)

fig.colorbar(surf)

plt.show()