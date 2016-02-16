import RPi.GPIO as GPIO

globalSetupDone = False

class Relay:
    def __init__(self, in_id, pin):
        self.pin = pin
        self.id = in_id
        GPIO.setup(self.id, GPIO.OUT)

    def TurnOn(self):
        GPIO.output(self.pin, FALSE)

    def TurnOff(self):
        GPIO.output(self.pin, True)

    def IsOn(self):
        input = GPIO.input(self.pin)


def GlobalSetup():
    global globalSetupDone
    if not globalSetupDone:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        globalSetupDone = True;

GlobalSetup()
