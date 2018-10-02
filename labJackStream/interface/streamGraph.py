from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool
from labJackStream.threadWorker import Worker
from multiprocessing import Queue
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
matplotlib.use('QT5Agg')


class StreamGraph(Canvas):
    def __init__(self):
        self.axes = [None]  # correction for only one plot with subplots
        self.fig, self.axes[0] = plt.subplots(1, facecolor=(0.3, 0.3, 0.3))

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

        self.normalize = False
        self.laserInit = 0
        self.timeWindow = 20
        self.maxY = 10
        self.minY = -1
        self.times = []
        self.laser = []
        self.transmitance = []
        self.reflectance = []

        self.lineLaser = None
        self.lineTransmitance = None
        self.lineReflectance = None
        self.graphQueue = Queue()
        self.tickLength = 2

        self.graphWorker = Worker(self.liveGraph)
        self.threadPool = QThreadPool()

    def startGraph(self):
        self.lineLaser, = self.axes[0].plot(self.times, self.laser, 'r')
        self.lineTransmitance, = self.axes[0].plot(self.times, self.transmitance, 'g')
        self.lineReflectance, = self.axes[0].plot(self.times, self.reflectance, 'b')

        self.axes[0].set_ylim(self.minY, self.maxY)
        self.axes[0].set_xlim(0, self.timeWindow)
        self.axes[0].set_xlabel("Time [s]", color="white")
        self.axes[0].tick_params(labelcolor="white")
        self.draw()

        self.threadPool.start(self.graphWorker)

    def liveGraph(self, statusSignal=None):
        data = self.graphQueue.get()
        laserSample, transmitanceSample, reflectanceSample = data
        self.laserInit = laserSample
        self.times.append(0)
        timeStart = time.time()

        while True:
            if self.normalize:
                normFactor = laserSample/self.laserInit
                transmitanceSample /= normFactor
                reflectanceSample /= normFactor
            self.laser.append(float(laserSample))
            self.transmitance.append(float(transmitanceSample))
            self.reflectance.append(float(reflectanceSample))

            # TODO: Get STDEV + normalize trs/ref data with laser deviation percentage
            # TODO: move files to DCCOTE repo

            self.updateLines()
            self.checkLimits()

            data = self.graphQueue.get()
            if len(data) == 0:
                break
            laserSample, transmitanceSample, reflectanceSample = data
            self.times.append(time.time() - timeStart)

        self.draw()

        self.printStats()
        self.saveData()

    def updateLines(self):
        self.lineLaser.set_xdata(self.times)
        self.lineLaser.set_ydata(self.laser)
        self.lineTransmitance.set_xdata(self.times)
        self.lineTransmitance.set_ydata(self.transmitance)
        self.lineReflectance.set_xdata(self.times)
        self.lineReflectance.set_ydata(self.reflectance)

    def checkLimits(self):
        if max(self.times) > self.timeWindow:
            self.axes[0].set_xlim(max(self.times) - self.timeWindow, max(self.times))

        if len(self.times) % self.tickLength == 0:
            self.updateLimits()

    def updateLimits(self):
        for vector in [self.laser, self.transmitance, self.reflectance]:
            if max(vector) > self.maxY:
                self.maxY = max(vector) + 0.5
                self.axes[0].set_ylim(self.minY, self.maxY)
            if min(vector) < self.minY:
                self.minY = min(vector) - 0.5
                self.axes[0].set_ylim(self.minY, self.maxY)
        self.draw()

    def printStats(self):
        print("\n|CHANNEL|    MIN|       MAX|       AVG|       STD|")
        for i, channel in enumerate([self.laser, self.transmitance, self.reflectance]):
            print("|{} |{:8.4f}|{:10.4f}|{:10.4f}|{:10.4f}|".format(["Laser", "Trans", "Refle"][i], np.min(channel), np.max(channel), np.average(channel), np.std(channel)))

    def saveData(self):
        dataArray = np.hstack((np.array(self.laser)[np.newaxis].T, np.array(self.transmitance)[np.newaxis].T))
        dataArray = np.hstack((dataArray, np.array(self.reflectance)[np.newaxis].T))

        index = 0
        fileName = "data"
        while os.path.exists(fileName + "{}.txt".format(index)):
            index += 1
        fileName = fileName + "{}.txt".format(index)

        np.savetxt(fileName, dataArray)
