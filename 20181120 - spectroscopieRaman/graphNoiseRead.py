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
readNoiseValue = 61634
thermalCoef = 8.97

readMean = []
thermalMean = []

for j, noiseFiles in enumerate([photonNoise]):  # readNoise, thermalNoise, photonNoise
    for i, file in enumerate(noiseFiles):
        data = getData(file)
        plt.plot(data[0], data[1], label="{}{}".format(["R", "T", "P"][j], i), linestyle=["-", "-.", "--"][j])

        if j == 0:
            readMean.append(np.round(np.mean(data[1]), 0))

        if j == 1:
            thermalMean.append(np.round(np.mean(data[1]) - readNoiseValue, 0))

print("READ NOISE: ", np.mean(readMean), readMean)
print("THERMAL NOISE: ", np.mean(thermalMean), thermalMean)
plt.ylabel("bits")
plt.xlabel("Pixels")
plt.legend()
plt.show()
