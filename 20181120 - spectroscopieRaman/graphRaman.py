import matplotlib.pyplot as plt
import numpy as np

"""❤😁💕💋💖🤳✨😃👀✔🐱‍🚀🥠🍜🥠🍜🥟🌮"""


class Raman:
    def __init__(self):
        self.fitPixels = True
        self.removeFluo = True

        self.oilFiles = ["data/{}.TXT".format(oil) for oil in ["mais", "arachide", "tournesol", "canola", "olive40m"]]
        self.oilNames = ["Maïs", "Arachide", "Tournesol", "Canola", "Olive"]
        self.integrationTimes = [100, 100, 100, 100, 4500]

        self.solFiles = ["data/{}.TXT".format(solution) for solution in ["ethanol", "isopropanol", "methanol", "glycerol", "sucrose"]]
        self.solNames = ["Éthanol", "Isopropanol", "Méthanol", "Glycérol", "Sucrose"]

        self.readNoiseValue = 61634
        self.thermalCoef = 8.97
        self.photonsPerBit = 4.35

        self.calibCoefs = []
        self.pixels = []
        self.waveNumbers = []
        self.intensities = []

        self.fileName = ""

    def graphOils(self):
        fig, axes = plt.subplots(len(self.oilFiles), sharex=True, sharey=False)

        self.setCalibration()

        for i, file in enumerate(self.oilFiles):
            pixel, intensity = self.getData(file)
            intensity -= self.readNoiseValue
            intensity -= self.thermalCoef * self.integrationTimes[i]
            intensity *= self.photonsPerBit
            intensity /= self.integrationTimes[i]

            waveNumber = self.translate(pixel)

            waveNumber, intensity = self.cut(waveNumber, intensity)

            fit = self.curveFit(waveNumber, intensity, degree=5, sections=1)

            raman = intensity - fit

            axes[i].plot(waveNumber, intensity)
            axes[i].plot(waveNumber, raman, label=self.oilNames[i])
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

    def graphSols(self):
        fig, axes = plt.subplots(len(self.solFiles), sharex=True, sharey=False)

        self.setCalibration()

        for i, file in enumerate(self.solFiles):
            pixel, intensity = self.getData(file)
            intensity -= self.readNoiseValue
            intensity -= self.thermalCoef * 100

            waveNumber = self.translate(pixel)

            waveNumber, intensity = self.cut(waveNumber, intensity, low=250, high=1600)

            fit = 0
            if i == 3 or 4:
                fit = self.curveFit(waveNumber, intensity, degree=2, sections=1)

            raman = intensity - fit
            raman /= 100
            raman *= self.photonsPerBit
            axes[i].plot(waveNumber, raman, label=self.solNames[i])
            axes[i].legend(handlelength=0, fontsize=12)
            axes[i].set_ylim(min(raman), 4000)
            axes[i].tick_params(labelsize=12)

            if i == 2:
                axes[i].set_ylabel("Intensité [p/s]", fontsize=13)

        plt.xlabel("Nombre d'onde [cm$^{-1}$]", fontsize=13)
        plt.xlim(250, 1600)
        fig.subplots_adjust(hspace=0, top=0.965, bottom=0.11, left=0.14, right=0.94, wspace=0.2)

        plt.show()

    def getFile(self):
        self.oilFiles = ["data/{}.TXT".format(oil) for oil in ["mais", "arachide", "tournesol", "canola", "olive40m"]]

        self.fileName = "data/{}".format(["mercury_27nov.txt", "ethanol.TXT", "olive40m.TXT", "canola.TXT", "mais.TXT",
                                          "arachide.TXT", "tournesol.TXT", "lampeMercure1.TXT"][6])

    @staticmethod
    def getData(fileName):
        pixels = []
        intensities = []
        with open(fileName, "r") as file:
            for line in file.readlines()[:-1]:
                data = line.split(",")[1:]
                pixels.append(float(data[0]))
                intensities.append(float(data[1]))
        return np.array(pixels), np.array(intensities)

    def setCalibration(self):
        mercure1 = [[588, 842.2, 1089.5, 1104.3], [671, 690, 708, 709]]
        mercure2 = [[587.5, 841, 1089, 1103.5], [671, 690, 708, 709]]
        # ethanol = [[571.2, 670.3, 697, 809.2, 927.2], self.wToLambda([879, 1050, 1085, 1279, 1450])]

        pixels = mercure1[0] + mercure2[0]
        wavelengths = mercure1[1] + mercure2[1]

        self.calibCoefs = np.polyfit(pixels, wavelengths, 1)

    def translate(self, pixels):
        [a, b] = self.calibCoefs
        wavelengths = np.array(pixels)*a + b
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

Raman().graphOils()
Raman().graphSols()
