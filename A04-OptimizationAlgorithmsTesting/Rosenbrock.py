"""
Actividad: 4. Funciones para probar algoritmos de optimizacion
Seminario de Inteligencia Artificial 1

- Rosenbrock
"""

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection = '3d')

X = np.arange(-2.048, 2.048, 0.1)
Y = np.arange(-2.048, 2.048, 0.1)

X, Y = np.meshgrid(X, Y)
