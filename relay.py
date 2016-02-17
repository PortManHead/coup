import RPi.GPIO as GPIO

globalSetupDone = False

class Relay:
    def __init__(self, in_id, pin):
        self.id = in_id
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def TurnOn(self):
        GPIO.output(self.pin, False)

    def TurnOff(self):
        GPIO.output(self.pin, True)

    def IsOn(self):
        return not GPIO.input(self.pin)


def GlobalSetup():
    global globalSetupDone
    if not globalSetupDone:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        globalSetupDone = True;

GlobalSetup()
