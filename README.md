SensorLog.py SETUP:
You must have a ~/.coup file with a dictionary mapping from your sensor number
to a (sensorType, gpioPin) tuple used for it.

For example, here is mine:

{1:(11,23), 2:(11,24), 3:(11,25), 4:(11,8)}
This shows that sensor #1 is a #11 type sensor, and it is attached to GPIO pin #23

This python program must be run with root priveledges.

