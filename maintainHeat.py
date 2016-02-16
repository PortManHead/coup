def MaintainHeat(sensor, relay, lowTemp, highTemp):
    sensor.CheckSensor()
    temp = sensor.Temp()
    print "HeatMaintainer:"
    print "    sensor=%s"   % sensor.Label()
    print "    relay=%s" % str(relay.id)
    print "    temp range: (%s, %s)" % (lowTemp, highTemp)
    print "    current temp: %s" % temp
    
    if temp < lowTemp:
        print "Temp too low. ",
        if relay.IsOn():
            print "Keeping heat on."
        else:
            print "Turning heat on."
            relay.TurnOn()

    elif temp > highTemp:
        print "Temp too high. ",
        if not relay.IsOn():
            print "Keeping heat off."
        else:
            print "Turning heat off."
            relay.TurnOff()

    else:
        print "Temp just right.  Leaving it",
        if relay.IsOn():
            print "on."
        else:
            print "off."

    

