import os
from sensor import Sensor
from relay import Relay

configLines = None


def GetSensors():
    configLines = GetConfigLines()
    sensorDict = eval(configLines[0])

    sensors = {}
    for key, value in sensorDict.iteritems():
        sensor = Sensor(key, value)
        sensors[key] = sensor
    return sensors

def GetRelays():
    configLines = GetConfigLines()
    relayDict = eval(configLines[1])

    relays = {}
    for key, value in relayDict.iteritems():
        relay = Relay(key, value)
        relays[key] = relay
    return relays


def GetConfigLines():
    global configLines
    if configLines:
        return configLines
    userName = os.environ["SUDO_USER"]
    homeDirectory = os.path.expanduser('~' + userName)
    configFile = os.path.join(homeDirectory, '.coup')
    configLines = open(configFile).readlines()

    return configLines

