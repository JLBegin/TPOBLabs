import matplotlib.pyplot as plt
import numpy as np

nbPhotons = np.linspace(1,100,1000)
bruitRelatif = []
bruitAbs = 1
for photons in nbPhotons:
    bruitRelatif.append((bruitAbs/photons )* 50)

plt.plot(nbPhotons,bruitRelatif)
plt.savefig('dataCorrection600dpi',dpi=600)
