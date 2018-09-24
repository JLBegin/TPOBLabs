import numpy as np
import matplotlib.pyplot as plt
import iadpython as iad

g = np.linspace(0.5, 0.8, 50)
plt.plot(g, iad.rt(1, 1, 0.5, 1.0, g))
plt.show()
