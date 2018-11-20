import matplotlib.pyplot as plt
import numpy as np

nbPhotons = np.linspace(1,80,1000)

bruitRelatif = 1/nbPhotons * 50

plt.xlabel("Nombre de bits")
plt.ylabel("Erreur relative (%)")
plt.plot(nbPhotons, bruitRelatif)

plt.savefig("bruitPhotons.png", dpi=600)
