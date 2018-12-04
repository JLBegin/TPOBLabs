import matplotlib.pyplot as plt
import numpy as np

"""❤😁💕💋💖🤳✨😃👀✔🐱‍🚀🥠🍜🥠🍜🥟🌮"""


class Raman:
    def __init__(self):
        self.removeFluo = True
        self.pixels = []
        self.waveNumbers = []
        self.intensities = []
        self.fit = []
        self.fileName = ""

    def graph(self):
        self.getFile()
        self.getData()
        self.normalize()
        self.pixelToWaveNumber()
        if self.removeFluo:
            self.curveFit(degree=40, sections=1)
        self.plot()

    def getFile(self):
        self.fileName = "data/{}".format(["mercury_27nov.txt", "ethanol.TXT", "olive40m.txt", "canola.TXT", "mais.TXT"][4])

    def getData(self):
        with open(self.fileName, "r") as file:
            for line in file.readlines()[:-1]:
                data = line.split(",")[1:]
                self.pixels.append(float(data[0]))
                self.intensities.append(float(data[1]))

    def normalize(self):
        self.intensities /= np.max(self.intensities)

    def pixelToWaveNumber(self):
        wavelength = [671, 690, 708, 709]
        pixel = [587.5, 841, 1089, 1103.5]
        [a, b] = np.polyfit(pixel, wavelength, 1)

        wavelengths = np.array(self.pixels)*a + b
        self.waveNumbers = 1/632.8 - 1/wavelengths
        self.waveNumbers *= 10**7

    def curveFit(self, degree, sections):
        for waveNumbers, intensities in zip(np.split(self.waveNumbers, sections), np.split(self.intensities, sections)):
            coefs = np.polyfit(waveNumbers, intensities, degree)
            self.fit.extend([np.sum([(waveNumber**i)*c for i, c in enumerate(reversed(coefs))]) for waveNumber in waveNumbers])

    def plot(self):
        plt.plot(self.waveNumbers, self.intensities, linewidth=2, label="Signal")

        if self.removeFluo:
            raman = self.intensities-self.fit
            plt.plot(self.waveNumbers, self.fit, label="Curve fit")
            plt.plot(self.waveNumbers, raman/np.max(raman*3), label="Difference")

        plt.ylabel("Intensity", fontsize=12)
        plt.xlabel("Wave number [1/cm]", fontsize=11)
        plt.legend(loc="best")
        plt.xlim(500, 2000)
        plt.tight_layout()
        plt.show()

Raman().graph()
