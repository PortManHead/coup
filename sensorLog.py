#!/usr/bin/python
import sys
import time
import Adafruit_DHT
import config

sensors = config.sensorPins


def Main():
    print TimeMessage()
    for sensorNum in sensors.keys():
        print SensorMessage(sensorNum)

def TimeMessage():
    return time.strftime("%d/%m/%Y %H:%M:%S")


def SensorMessage(sensorNum):
    temp, humidity = GetTempHumidity(sensors[sensorNum])
    msg = "Sensor #%d: %.0f deg F, %.0f%% humidity" % (sensorNum, temp, humidity)
    return msg


def GetTempHumidity((sensorType, pin)):
    sensor_args = { 11: Adafruit_DHT.DHT11,
		    22: Adafruit_DHT.DHT22,
		    2302: Adafruit_DHT.AM2302 }

    sensor = sensor_args[sensorType]

    humidity, tempC = Adafruit_DHT.read_retry(sensor, pin)
    tempF = CTempToF(tempC)

    return tempF, humidity


def CTempToF(c):
    f = (c * 1.8) + 32
    return f



if __name__ == "__main__":
    Main()
