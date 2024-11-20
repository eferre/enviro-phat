from sys import exit, version_info

try:
    import smbus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

bus = None
try:
    import RPi.GPIO as GPIO
    if GPIO.RPI_REVISION == 2 or GPIO.RPI_REVISION == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)
except ImportError:
    bus = smbus.SMBus(1)
