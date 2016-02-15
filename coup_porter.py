#!/usr/bin/python
import sys
import time
import Adafruit_DHT
import sensors
import RPi.GPIO as GPIO

sensors = sensors.GetSensors()

relay1 = 4
relay2 = 17
relay3 = 22
relay4 = 27
relays = [relay1, relay2, relay3, relay4]

def Main():
    SetupRelays()
    print TimeMessage() 
    for num, sensor in sensors.iteritems():
        print sensor.LogMessage()

    MaintainHeat(sensors[1], relay1, 45, 55)

def SetupRelays():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for relay in relays:
        GPIO.setup(relay, GPIO.OUT)

def MaintainHeat(sensor, relay, lowTemp, highTemp):
    sensor.CheckSensor()
    print "MaintainHeat:  sensor=%s, relay=%d, lowTemp=%d, highTemp=%d, currentTemp=%d" % \
            (sensor.Label(), relay, lowTemp, highTemp, sensor.temp)
    if sensor.temp < lowTemp:
        TurnRelayOn(relay)
        print "Too low.  Turning on heat"
    elif sensor.temp > highTemp:
        TurnRelayOff(relay)
        print "Too high.  Turning off heat"
    else:
        print "Just right.  Leaving it be."

    
def TurnRelayOn(relay):
     GPIO.output(relay, False)

def TurnRelayOff(relay):
     GPIO.output(relay, True)


def TimeMessage():
    return time.strftime("%d/%m/%Y %H:%M:%S")






if __name__ == "__main__":
    Main()
