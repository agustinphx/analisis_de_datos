import matplotlib.pyplot as plt
import numpy as np

mu = [-2, 2]                          # Valores medios de x e y
cxy = [[1, 1], [1, 2]]               # Matriz de covarianza, [[Cxx, Cxy], [Cyx, Cyy]]
N = 100
x, y = np.random.multivariate_normal(mu, cxy, N).T

plt.scatter(x, y,s = (10 * np.random.rand(N))**2, alpha=0.5)

plt.show()
