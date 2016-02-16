import os
import Adafruit_DHT

class Sensor:
    def __init__(self, num, values):
        self.num = num
        self.sensorType = values[0]
        self.pin = values[1]
        self.name = ""
        if(len(values) >= 3):
            self.name = values[2]
        self._temp = -1
        self._humidity = -1
        self.sensorChecked = False

    def Temp(self):
        self.CheckSensor()
        return self._temp

    def Humidity(self):
        self.CheckSensor()
        return self._humidity




    def CheckSensor(self):
        if not self.sensorChecked:
            sensor_args = { 11: Adafruit_DHT.DHT11,
                            22: Adafruit_DHT.DHT22,
                            2302: Adafruit_DHT.AM2302 }
    
            sensor = sensor_args[self.sensorType]
    
            self._humidity, tempC = Adafruit_DHT.read_retry(sensor, self.pin)
            self._temp = CTempToF(tempC)
            self.sensorChecked = True



    def LogMessage(self):
        msg = "%s %s deg F" % (self.Label(), self.Temp())
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
