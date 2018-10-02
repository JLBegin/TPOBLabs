"""
** From LabJack API's examples **

This example uses Python's built-in threading module to help reach faster
streaming speeds than streamTest.py.
"""

import sys
import threading
import time

from copy import deepcopy
from datetime import datetime

try:
    import Queue
except ImportError:  # Python 3
    import queue as Queue

import u3


# self.MAX_REQUESTS is the number of packets to be read.


class StreamLabJack:
    def __init__(self, graph):
        self.graph = graph
        self.data = Queue.Queue()
        self.dataCount = 0
        self.missed = 0
        self.finished = False
        self.sdrThread = None
        self.processThread = None
        self.MAX_REQUESTS = 2500
        self.SCAN_FREQUENCY = 50000
        self.device = None
        self.device = None
        self.initLabJack()

    def initLabJack(self):
        self.device = u3.U3()
        self.device.configU3()
        self.device.getCalibrationData()

        # Set the FIO0 to Analog
        self.device.configIO(FIOAnalog=1)

        print("Configuring U3 stream")
        self.device.streamConfig(NumChannels=1, PChannels=[0], NChannels=[31], Resolution=3, ScanFrequency=self.SCAN_FREQUENCY)

        if self.device is None:
            print("""Configure a device first.
        Please open streamTest-threading.py in a text editor and uncomment the lines for your device.

        Exiting...""")
            sys.exit(0)

        print("Configured !")

    def startStream(self):
        # writing at the DAC0
        self.device.writeRegister(5000, 3)
        self.sdrThread = threading.Thread(target=self.readStreamData)
        self.processThread = threading.Thread(target=self.processStreamData)

        self.sdrThread.start()
        self.graph.startGraph()
        self.processThread.start()

    def readStreamData(self):
        self.finished = False

        print("Start stream.")
        start = datetime.now()
        try:
            self.device.streamStart()
            while not self.finished:
                returnDict = next(self.device.streamData(convert=False))

                if returnDict is None:
                    print("No stream data")
                    continue

                self.data.put_nowait(deepcopy(returnDict))

                self.missed += returnDict["missed"]
                self.dataCount += 1
                if self.dataCount >= self.MAX_REQUESTS:
                    self.finished = True

            print("Stream stopped.\n")
            self.device.streamStop()
            stop = datetime.now()

            # Delay to help prevent print text overlapping in the two threads.
            time.sleep(0.200)

            sampleTotal = self.dataCount * self.device.packetsPerRequest * self.device.streamSamplesPerPacket

        except Exception:
            try:
                # Try to stop stream mode. Ignore exception if it fails.
                self.device.streamStop()
            except:
                pass
            self.finished = True
            e = sys.exc_info()[1]
            print("readStreamData exception: %s %s" % (type(e), e))

    def processStreamData(self):
        errors = 0
        missed = 0
        while True:
            try:
                result = self.data.get(True, 1)

                if result["errors"] != 0:
                    errors += result["errors"]
                    missed += result["missed"]
                    print("+++++ Total Errors: %s, Total Missed: %s +++++" % (errors, missed))

                # Convert the raw bytes (result['result']) to voltage data.
                r = self.device.processStreamData(result['result'])

                # Do some processing on the data to show off.
                # print("DICT R: ", r, r.keys())
                pinAIN0 = sum(r['AIN0']) / len(r['AIN0'])
                # print("Average of %s reading(s): %s" % (len(r['AIN0']), pinAIN0))

                graphData = [pinAIN0, pinAIN0-0.1, pinAIN0+0.1]
                self.graph.graphQueue.put(graphData)

            except Queue.Empty:
                if self.finished:
                    print("Done reading from the Queue.")
                else:
                    print("Queue is empty. Stopping...")
                    self.finished = True
                break
            except KeyboardInterrupt:
                self.finished = True
            except Exception:
                e = sys.exc_info()[1]
                print("main exception: %s %s" % (type(e), e))
                self.finished = True
                break

    def stopStream(self):
        self.data.put([])
        self.graph.graphQueue.put([])
        self.sdrThread.join()
        # Close the device
        self.device.close()

