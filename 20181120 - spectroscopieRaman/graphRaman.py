import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

"""❤😁💕💋💖🤳✨😃👀✔🐱‍🚀🥠🍜🥠🍜🥟🌮"""


class Raman:
    def __init__(self):
        self.fitPixels = True
        self.removeFluo = True

        self.oilFiles = ["data/{}.TXT".format(oil) for oil in ["mais", "arachide", "tournesol", "canola", "olive40m"]]
        self.oilNames = ["Maïs", "Arachide", "Tournesol", "Canola", "Olive"]
        self.integrationTimes = [100, 100, 100, 100, 1200*2]
        self.numberOfAcq = [100, 100, 100, 100, 1200]

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
            # intensity -= self.readNoiseValue * self.numberOfAcq[i]
            intensity -= self.thermalCoef * self.integrationTimes[i]

            waveNumber = self.translate(pixel)

            waveNumber, intensity = self.cut(waveNumber, intensity)

            fit = self.curveFit(waveNumber, intensity, degree=5, sections=1)

            raman = intensity - fit
            raman /= self.integrationTimes[i]
            raman *= self.photonsPerBit
            # raman -= np.mean(raman)
            # raman /= np.max(raman*10)
            axes[i].plot(waveNumber, raman, label=self.oilNames[i])
            axes[i].legend(handlelength=0, fontsize=12)
            axes[i].set_ylim(min(raman), 3200)
            axes[i].tick_params(labelsize=12)
            if i == 2:
                axes[i].set_ylabel("Intensité [p/s]", fontsize=13)

        plt.xlabel("Nombre d'onde [cm$^{-1}$]", fontsize=13)
        plt.xlim(1200, 1850)
        fig.subplots_adjust(hspace=0, top=0.965, bottom=0.11, left=0.14, right=0.94, wspace=0.2)

        plt.show()

    def graphSols(self):
        fig, axes = plt.subplots(len(self.solFiles), sharex=True, sharey=False)

        self.setCalibration()

        for i, file in enumerate(self.solFiles):
            pixel, intensity = self.getData(file)
            # intensity -= self.readNoiseValue * 100
            intensity -= self.thermalCoef * 100

            waveNumber = self.translate(pixel)

            waveNumber, intensity = self.cut(waveNumber, intensity, low=250, high=1600)

            fit = 0
            if i == 3 or 4:
                fit = self.curveFit(waveNumber, intensity, degree=2, sections=1)

            raman = intensity - fit
            raman /= 100
            raman *= self.photonsPerBit
            # raman -= np.mean(raman)
            # raman /= np.max(raman*10)
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

    def plot(self):
        xlim = 2000

        if not self.fitPixels:
            self.waveNumbers = self.pixels
            xlim = 1300

        plt.plot(self.waveNumbers, self.intensities, linewidth=2, label="Signal")

        if self.removeFluo:
            diff = (self.intensities-self.fit)
            raman = diff/np.max(diff*10)
            plt.plot(self.waveNumbers, self.fit, label="Curve fit")
            plt.plot(self.waveNumbers, raman, label="Difference")

        plt.ylim(min(raman))
        N = len(self.intensities)
        fZ = np.fft.fft(self.intensities)
        # # fZ = fftpack.fftshift(np.abs(fZ))
        fr = np.linspace(-N/1.6, N/1.6, N)

        fZ[np.where(np.abs(fr) > 800)] = 0
        fZ[np.where(np.abs(fr) < 0)] = 0

        waves = np.fft.ifft(fZ)

        # plt.plot(fr, fZ, label='fft')

        # plt.plot(self.waveNumbers, np.abs(waves), label="ifft")

        plt.ylabel("Intensity", fontsize=12)
        plt.xlabel("Wave number [1/cm]", fontsize=11)
        plt.legend(loc="best")
        # plt.xlim(500, xlim)
        plt.tight_layout()
        plt.show()

Raman().graphOils()

Raman().graphSols()
