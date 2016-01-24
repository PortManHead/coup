import os



userName = os.environ["SUDO_USER"]
homeDirectory = os.path.expanduser('~' + userName)
configFile = os.path.join(homeDirectory, '.coup')
configLines = open(configFile).readlines()

sensorPins = eval(configLines[0])

