import numpy as np
import matplotlib.pyplot as plt


class DataGraph:
    def __init__(self):
        self.rawData = []
        self.normData = []
        self.smoothFactor = 10  # How much values to avg ( > 0 )
        self.fig, self.axes = plt.subplots(2, figsize=(15, 10))

    def compareCorrectedData(self):
        self.getData()
        self.plotData()
        self.adjustPlot()
        self.show()

    def getData(self):
        self.rawData = np.loadtxt("./data/readingRaw300sec1.txt")
        self.normData = np.loadtxt("./data/readingNorm300sec.txt")

    def plotData(self):
        for e, data in enumerate([self.normData, self.normData]):  # Fastest and ugliest data back correction
            numberOfColumns = data[0].shape[0] - 1
            timeVector = data[:, 0][::self.smoothFactor] - 100

            for i in range(numberOfColumns):
                normData = data[:, i+1]
                if e == 0 and i > 0:
                    rawFactor = data[:, 1] / data[:, 1][0]
                    normData = data[:, i+1] * rawFactor

                normData /= np.mean(normData)
                stDev = round(np.std(normData)*100, 2)
                if self.smoothFactor > 1:
                    normData = (normData - 1) * 100
                    normData = [np.mean(normData[i*self.smoothFactor:(i+1)*self.smoothFactor]) for i in range((len(normData)//self.smoothFactor)+1)]
                self.axes[e].plot(timeVector, normData, label="{} ($\sigma$ = {}%)".format(["Source laser", "Transmitance", "Réflectance"][i], stDev), color=["r", "g", "b"][i], linestyle=["-", "-"][e])

    def adjustPlot(self):
        for axe in self.axes:
            axe.set_xlim(0, 150)
            axe.set_ylim(-2, 4)
            axe.set_ylabel("Intensité relative", fontsize=17)
            axe.set_xlabel("Temps [s]", fontsize=17)
            axe.legend(loc="upper right", fontsize=15)
            axe.tick_params(labelsize=16, length=8, width=2)
            axe.axhline(0, color="black")
            axe.axhline(-2, color="black", linewidth=3)
            axe.axhline(4, color="black", linewidth=3)
            axe.axvline(0, color="black", linewidth=3)
            axe.axvline(150, color="black", linewidth=3)
        plt.tight_layout(h_pad=3)

    def show(self):
        plt.savefig('dataCorrection600dpi',dpi=600)
        plt.show()


DataGraph().compareCorrectedData()
