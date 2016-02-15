import os
import Adafruit_DHT

def GetSensors():
    userName = os.environ["SUDO_USER"]
    homeDirectory = os.path.expanduser('~' + userName)
    configFile = os.path.join(homeDirectory, '.coup')
    configLines = open(configFile).readlines()
    
    sensorConfig = eval(configLines[0])

    sensors = {}
    for key, value in sensorConfig.iteritems():
        sensor = Sensor(key, value)
        sensors[key] = sensor
    return sensors



class Sensor:
    def __init__(self, num, values):
        self.num = num
        self.sensorType = values[0]
        self.pin = values[1]
        self.name = ""
        if(len(values) >= 3):
            self.name = values[2]
        self.temp = -1
        self.humidity = -1
        self.CheckSensor()


    def CheckSensor(self):
        sensor_args = { 11: Adafruit_DHT.DHT11,
                        22: Adafruit_DHT.DHT22,
                        2302: Adafruit_DHT.AM2302 }

        sensor = sensor_args[self.sensorType]

        self.humidity, tempC = Adafruit_DHT.read_retry(sensor, self.pin)
        self.temp = CTempToF(tempC)



    def LogMessage(self):
        msg = "%s %.0f deg F, %.0f%% humidity" % \
                (self.Label(), self.temp, self.humidity)
        return msg

    def Label(self):
        label = "Sensor #%d" % self.num
        if self.name:
            label += " (%s)" % self.name
        label += ":"
        return label



def CTempToF(c):
    f = (c * 1.8) + 32
    return f
