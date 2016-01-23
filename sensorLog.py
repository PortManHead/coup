#!/usr/bin/python
import sys
import time
import Adafruit_DHT

sensorPins = {1:23, 2:24, 3:25, 4:8}


def Main():
    print TimeMessage()
    for sensorNum in sensorPins.keys():
        print SensorMessage(sensorNum)

def TimeMessage():
    return time.strftime("%d/%m/%Y %H:%M:%S")


def SensorMessage(sensorNum):
    temp, humidity = GetTempHumidity(sensorPins[sensorNum])
    msg = "Sensor #%d: %.0f deg F, %.0f%% humidity" % (sensorNum, temp, humidity)
    return msg


def GetTempHumidity(pin, sensorNum='11'):
# Parse command line parameters.
    sensor_args = { '11': Adafruit_DHT.DHT11,
		    '22': Adafruit_DHT.DHT22,
		    '2302': Adafruit_DHT.AM2302 }

    sensor = sensor_args[sensorNum]

    humidity, tempC = Adafruit_DHT.read_retry(sensor, pin)
    tempF = CTempToF(tempC)

    return tempF, humidity


def CTempToF(c):
    f = (c * 1.8) + 32
    return f




if __name__ == "__main__":
    Main()
