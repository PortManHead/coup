#! /usr/bin/env python
import time
import RPi.GPIO as GPIO

relay1=4
relay2=17
relay3=22
relay4=27
    
relays=[relay1, relay2, relay3, relay4]

def TurnRelayOn(relay):
    GPIO.output(relay, False)


def TurnRelayOff(relay):
    GPIO.output(relay, True)

def RelayOnForDuration(relay, duration):
    TurnRelayOn(relay)
    print "%d on" % (relay)
    time.sleep(duration)
    TurnRelayOff(relay)
    print "%d off" % (relay)


def Flash(relay, on, off, repeat):
    for i in range(repeat):
        TurnRelayOn(relay)
        time.sleep(on)
        TurnRelayOff(relay)
        time.sleep(off)


def Setup():
    relay1=4
    relay2=17
    relay3=22
    relay4=27
    
    relays=[relay1, relay2, relay3, relay4]
    
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.setup(relay2, GPIO.OUT)
    GPIO.setup(relay3, GPIO.OUT)
    GPIO.setup(relay4, GPIO.OUT)


def Main():
    Setup()

    for i in range(10):
        for relay in relays:
            RelayOnForDuration(relay, 0.5)

Main()



