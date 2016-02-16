#!/usr/bin/python
import sys
import time
import Adafruit_DHT
import config
import RPi.GPIO as GPIO
from maintainHeat import MaintainHeat

sensors = config.GetSensors()
relays = config.GetRelays()


def Main():
    print TimeMessage() 
    for num, sensor in sensors.iteritems():
        print sensor.LogMessage()

    MaintainHeat(sensors[1], relays[1], 45, 55)


def TimeMessage():
    return time.strftime("----\n%d/%m/%Y %H:%M:%S")






if __name__ == "__main__":
    Main()
