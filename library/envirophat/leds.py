from sys import exit

gpio_sel = None
try:
    import RPi.GPIO as GPIO
    gpio_sel = True
except ImportError:
    import gpiozero
    gpio_sel = False

pin = None
if gpio_sel:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, 0)
else:
    pin = gpiozero.LED(4)
    pin.off()
    

class leds:
    def __init__(self, status=0):
        self.status = status

    def on(self):
        """Turn LEDs on."""
        self.status = 1
        if gpio_sel:
            GPIO.output(4, 1)
        else:
            pin.on()
        return True

    def off(self):
        """Turn LEDs off."""
        self.status = 0
        if gpio_sel:
            GPIO.output(4, 0)
        else:
            pin.off()

    def is_on(self):
        """Return True if LED is on."""
        if self.status == 1:
            return True
        else:
            return False

    def is_off(self):
        """Return True if LED is off."""
        if self.status == 0:
            return True
        else:
            return False
