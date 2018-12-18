import matplotlib.pyplot as plt
import numpy as np

readNoise = ["data/bruitMesure{}.TXT".format(i) for i in range(9)]
thermalNoise = ["data/bruitThermique{}.TXT".format(i) for i in range(6)]
photonNoise = ["data/bruitPhoton{}.TXT".format(i) for i in range(5)]


def getData(fileName):
    pixels = []
    intensities = []
    with open(fileName, "r") as file:
        for line in file.readlines()[:-1]:
            data = line.split(",")[1:]
            pixels.append(float(data[0]))
            intensities.append(float(data[1]))

    return pixels[200: 1200], intensities[200: 1200]

photonTimes = [0.001, 0.1, 1, 5, 10]
readNoiseValue = 61550
thermalCoef = 8.97
photonsPerBit = 4.35

readMean = []
thermalMean = []

for j, noiseFiles in enumerate([readNoise]):  # readNoise, thermalNoise, photonNoise
    means = []
    for i, file in enumerate(noiseFiles):
        data = getData(file)
        means.append(np.mean(data[1])*4.35)
        plt.plot(data[0], data[1], label="{} s".format([1, 5, 10, 25, 50, 100][i]), linestyle=["-", "-.", "--"][j])  # ["R", "T", "P"][j]

        if j == 0:
            readMean.append(np.round(np.mean(data[1]), 0))

        if j == 1:
            thermalMean.append(np.round(np.mean(data[1]) - readNoiseValue, 0))

    plt.plot([0.001, 0.01, 0.1, 1, 5, 10, 25, 50, 100], means, label="$L \\approx 2.681 \\times 10^5 \pm 0.001$", linewidth=0, marker=".", markersize=9)  # [1, 5, 10, 25, 50, 100]

print("READ NOISE: ", np.mean(readMean), readMean)
print("THERMAL NOISE: ", np.mean(thermalMean), thermalMean)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
plt.ylabel("Nombre de photons")
plt.xlabel("Temps d'intégration [ms]")
plt.ylim(267800, 268400)
plt.semilogx()
plt.legend(fontsize=11)
plt.show()
