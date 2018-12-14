import matplotlib.pyplot as plt
import numpy as np

"""❤😁💕💋💖🤳✨😃👀✔🐱‍🚀🥠🍜🥠🍜🥟🌮"""


class Raman:
    def __init__(self):
        self.fitPixels = True
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
        self.calibrate()
        if self.removeFluo:
            self.curveFit(degree=3, sections=10)
        self.plot()

    def getFile(self):
        self.fileName = "data/{}".format(["mercury_27nov.txt", "ethanol.TXT", "olive40m.txt", "canola.TXT", "mais.TXT", "lampeMercure1.TXT"][2])

    def getData(self):
        with open(self.fileName, "r") as file:
            for line in file.readlines()[:-1]:
                data = line.split(",")[1:]
                self.pixels.append(float(data[0]))
                self.intensities.append(float(data[1]))

    def normalize(self):
        self.intensities /= np.max(self.intensities)

    def calibrate(self):
        mercure1 = [[588, 842.2, 1089.5, 1104.3], [671, 690, 708, 709]]
        mercure2 = [[587.5, 841, 1089, 1103.5], [671, 690, 708, 709]]
        # ethanol = [[571.2, 670.3, 697, 809.2, 927.2], self.wToLambda([879, 1050, 1085, 1279, 1450])]

        pixels = mercure1[0] + mercure2[0]
        wavelengths = mercure1[1] + mercure2[1]

        [a, b] = np.polyfit(pixels, wavelengths, 1)

        wavelengths = np.array(self.pixels)*a + b
        self.waveNumbers = 1/632.8 - 1/wavelengths
        self.waveNumbers *= 10**7

    @staticmethod
    def wToLambda(waveNumbers):
        return [np.round(((1/632.8 - w*10**(-7))**(-1)), 2) for w in waveNumbers]

    def curveFit(self, degree, sections):
        for waveNumbers, intensities in zip(np.split(self.waveNumbers, sections), np.split(self.intensities, sections)):

            coefs = np.polyfit(waveNumbers, intensities, degree)
            self.fit.extend([np.sum([(waveNumber**i)*c for i, c in enumerate(reversed(coefs))]) for waveNumber in waveNumbers])

    def plot(self):
        xlim = 2000

        if not self.fitPixels:
            self.waveNumbers = self.pixels
            xlim = 1300

        plt.plot(self.waveNumbers, self.intensities, linewidth=2, label="Signal")

        if self.removeFluo:
            raman = self.intensities-self.fit
            plt.plot(self.waveNumbers, self.fit, label="Curve fit")
            plt.plot(self.waveNumbers, raman/np.max(raman*3), label="Difference")

        plt.ylabel("Intensity", fontsize=12)
        plt.xlabel("Wave number [1/cm]", fontsize=11)
        plt.legend(loc="best")
        plt.xlim(500, xlim)
        plt.tight_layout()
        plt.show()

Raman().graph()
