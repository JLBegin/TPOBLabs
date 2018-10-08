import numpy as np
import matplotlib.pyplot as plt


class DataGraph:
    def __init__(self):
        self.rawData = []
        self.normData = []
        self.smoothFactor = 10  # How much values to avg ( > 0 )

    def compareCorrectedData(self):
        self.getData()
        self.plotData()
        self.show()

    def getData(self):
        self.rawData = np.loadtxt("../labJackStream/data/readingRaw300sec1.txt")
        self.normData = np.loadtxt("../labJackStream/data/readingNorm300sec.txt")

    def plotData(self):
        for e, data in enumerate([self.rawData, self.normData]):

            numberOfColumns = data[0].shape[0] - 1
            timeVector = data[:, 0][::self.smoothFactor]

            for i in range(numberOfColumns):
                normData = data[:, i+1] / np.mean(data[:, i+1])
                if self.smoothFactor > 1:
                    normData = [np.mean(normData[i*self.smoothFactor:(i+1)*self.smoothFactor]) for i in range((len(normData)//self.smoothFactor)+1)]
                plt.plot(timeVector, normData, label=["Incidence", "Transmitance", "Réflectance"][i], color=["r", "g", "b"][i], linestyle=["--", "-"][e])

    def show(self):
        plt.legend(loc="best")
        plt.show()

DataGraph().compareCorrectedData()
