#! /cygdrive/c/python35/python.exe
import datetime
import ephem
from pytz import timezone
import pytz

class Sunrise():
    def __init__(self, lat, long):
        self._location = ephem.Observer()
        self._location.lat = lat
        self._location.long = long
        self._sun = ephem.Sun()
        self._sun.compute()

    def NextSunrise(self):
        return self._location.next_rising(self._sun).datetime()

    def NextSunset(self):
        return self._location.next_setting(self._sun).datetime()

    def TimeUntilNextSunrise(self):
        return self.NextSunrise() - datetime.datetime.now()

    def TimeUntilNextSunset(self):
        return self.NextSunset() - datetime.datetime.now()

    def IsDaytime(self):
        return self.TimeUntilNextSunset() < self.TimeUntilNextSunrise()
            




if __name__=="__main__":
     s = Sunrise("44.943004", "-123.372055")
     print(s.NextSunrise())
     print(s.NextSunset())
     print(s.TimeUntilNextSunrise())
     print(s.TimeUntilNextSunset())
     print(s.IsDaytime())
        





