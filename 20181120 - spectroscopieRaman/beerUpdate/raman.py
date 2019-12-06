import numpy as np
import matplotlib.pyplot as plt

"""
Spin-off of main graphRaman.py file.
Used to load pre-calibrated files of wavelength (in descending order) & intensity
*The cut window and the graphs have not yet been optimized for the beer data.
"""


class Raman:
    def __init__(self):
        self.fitPixels = True
        self.removeFluo = True

        self.beerFiles = ["data/{}.txt".format(beerName) for beerName in ["tremblay", "coors"]]
        self.beerNames = ["Tremblay", "Coors"]
        self.integrationTimes = [150, 100]

        self.readNoiseValue = 62825
        self.thermalCoef = 1.683
        self.photonsPerBit = 4.35

        self.calibCoefs = []
        self.wavelengths = []
        self.waveNumbers = []
        self.intensities = []

        self.fileName = ""

    def graphBeer(self):
        fig, axes = plt.subplots(len(self.beerFiles), sharex=True, sharey=False)

        for i, file in enumerate(self.beerFiles):
            wavelength, intensity = self.getData(file)
            intensity -= self.readNoiseValue
            intensity -= self.thermalCoef * self.integrationTimes[i]
            intensity *= self.photonsPerBit
            intensity /= self.integrationTimes[i]

            waveNumber = self.translate(wavelength)

            waveNumber, intensity = self.cut(waveNumber, intensity)

            fit = self.curveFit(waveNumber, intensity, degree=5, sections=1)

            raman = intensity - fit

            axes[i].plot(waveNumber, intensity)
            axes[i].plot(waveNumber, raman, label=self.beerNames[i])
            axes[i].legend(handlelength=0, fontsize=12)
            axes[i].set_ylim(min(raman), 3200)
            axes[i].tick_params(labelsize=12)

            print("STD ", i, np.std(raman[200:220]))

            if i == 2:
                axes[i].set_ylabel("Intensité [p/s]", fontsize=13)

            if i == 6:  # i == 4  : Last resort ploting
                plt.show()

                ax1 = plt.subplot2grid((5, 2), (0, 0), rowspan=3, colspan=2)
                ax2 = plt.subplot2grid((5, 2), (3, 0))
                ax3 = plt.subplot2grid((5, 2), (3, 1))
                ax4 = plt.subplot2grid((5, 2), (4, 0), colspan=2)
                ax1.plot(waveNumber, intensity, label="Signal total")
                ax1.plot(waveNumber, fit, label="Curve-fit")
                ax2.plot(waveNumber, intensity, label="Signal total")
                ax2.plot(waveNumber, fit, label="Curve-fit")
                ax3.plot(waveNumber, intensity, label="Signal total")
                ax3.plot(waveNumber, fit, label="Curve-fit")
                ax4.plot(waveNumber, raman, label="Signal Raman")

                ax2.set_ylabel("Intensité [p/s]", fontsize=13)
                ax4.set_xlabel("Nombre d'onde [cm$^{-1}$]", fontsize=13)
                ax1.set_xlim(1200, 1850)
                ax2.set_xlim(1200, 1450)
                ax3.set_xlim(1500, 1850)
                ax4.set_xlim(1200, 1850)
                ax1.legend()
                ax3.legend()
                ax4.legend()
                ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
                ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
                ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
                plt.show()

        plt.xlabel("Nombre d'onde [cm$^{-1}$]", fontsize=13)
        plt.xlim(1200, 1850)
        fig.subplots_adjust(hspace=0, top=0.965, bottom=0.11, left=0.14, right=0.94, wspace=0.2)

        plt.show()

    def getFile(self):
        self.beerFiles = ["data/{}.txt".format(beer) for beer in ["tremblay", "coors"]]

        self.fileName = "data/{}".format(["mercury_27nov.txt", "ethanol.TXT", "olive40m.TXT", "canola.TXT", "mais.TXT",
                                          "arachide.TXT", "tournesol.TXT", "lampeMercure1.TXT"][6])

    @staticmethod
    def getData(fileName):
        wavelengths = []
        intensities = []
        with open(fileName, "r") as file:
            for line in reversed(file.readlines()[:-1]):
                data = line.split()
                wavelengths.append(float(data[0]))
                intensities.append(float(data[1]))
        return np.array(wavelengths), np.array(intensities)

    def translate(self, wavelengths):
        waveNumbers = 1/632.8 - 1/wavelengths
        return waveNumbers * 10**7

    @staticmethod
    def wToLambda(waveNumbers):
        return [np.round(((1/632.8 - w*10**(-7))**(-1)), 2) for w in waveNumbers]

    def cut(self, waveNumbers, intensities, low=1200, high=1850):
        start = np.where(waveNumbers > low)[0][0]
        end = np.where(waveNumbers > high)[0][0]
        return waveNumbers[start: end], intensities[start: end]

    @staticmethod
    def curveFit(waveNumbers, intensities, degree, sections):
        fit = []
        for waveNumbers, intensities in zip(np.split(waveNumbers, sections), np.split(intensities, sections)):

            coefs = np.polyfit(waveNumbers, intensities, degree)
            fit.extend([np.sum([(waveNumber**i)*c for i, c in enumerate(reversed(coefs))]) for waveNumber in waveNumbers])
        return fit

    @staticmethod
    def save(waveNumbers, intensities):
        col1 = np.array(waveNumbers)[np.newaxis].T
        col2 = np.array(intensities)[np.newaxis].T
        data = np.hstack((col1, col2))

        np.savetxt("outputRaman.txt", data, '%.15f')


Raman().graphBeer()
