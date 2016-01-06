#! /usr/bin/env python
import time
import RPi.GPIO as GPIO

relay1=4
relay2=17
relay3=22
relay4=27
relays=[relay1, relay2, relay3, relay4]
    


def SwitchRelay(relay, value):
    GPIO.output(relay, False if value else True)


def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(relay1, GPIO.OUT)
    GPIO.setup(relay2, GPIO.OUT)
    GPIO.setup(relay3, GPIO.OUT)
    GPIO.setup(relay4, GPIO.OUT)
    


def Main():
    Setup()

    for relay in relays:
        SwitchRelay(relay, True)
        time.sleep(1)
        SwitchRelay(relay, False)
        time.sleep(1)



Main()



