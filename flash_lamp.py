#! /usr/bin/env python
import time
import RPi.GPIO as GPIO

<<<<<<< HEAD
relay1=4
relay2=17
relay3=22
relay4=27
    
relays=[relay1, relay2, relay3, relay4]

=======
>>>>>>> 7cdd7bae4242c795cd9731faecf74b2012294fcb

def SwitchRelay(relay, value):
    GPIO.output(relay, False if value else True)


<<<<<<< HEAD
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
=======
def Setup():
    relay1=4
    relay2=17
    relay3=22
    relay4=27
    
    relays=[relay1, relay2, relay3, relay4]
    
    
>>>>>>> 7cdd7bae4242c795cd9731faecf74b2012294fcb
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(relay1, GPIO.OUT)
    GPIO.setup(relay2, GPIO.OUT)
    GPIO.setup(relay3, GPIO.OUT)
    GPIO.setup(relay4, GPIO.OUT)


<<<<<<< HEAD
def Main():
    Setup()

    #for relay in relays:
        #TurnRelayOn(relay)
    #return 1

    for i in range(10):
        for relay in relays:
            RelayOnForDuration(relay, 5.5)

    #Flash(relay4, 0.3, 1.0, 5)

    #for relay in relays:
    #    Flash(relay, 0.3, 1.0, 1)

    
    
=======

def Main():

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


	
    #for relay in relays:
        #SwitchRelay(relay, True)
        #time.sleep(1)
        #SwitchRelay(relay, False)
        #time.sleep(1)


    for i in range(10000):
        print "ON"
        SwitchRelay(relay1, True)
        time.sleep(.3)
        print "OFF"
        SwitchRelay(relay1, False)
        time.sleep(2 * 60 - 0.2)
		
>>>>>>> 7cdd7bae4242c795cd9731faecf74b2012294fcb

Main()



