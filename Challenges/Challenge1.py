import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=-1, stop=1, num=5)
plt.plot(x, np.absolute(x))

plt.show()
