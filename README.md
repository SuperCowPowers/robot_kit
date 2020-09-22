# robot_kit
Having fun with the Freenove 4WD Smart Car Kit

### Install
SSH to your Raspberry Pi and install the Python module for Python 3.

```
$ sudo pip3 install robot_kit
```

### Examples
See the Examples directory for all the code, here are some short examples of how to use the module.

```
from robot_kit.leds import NeoPixelStrip
from robot_kit.wheels import Wheels
import time

if __name__ == '__main__':
    """Run some of the basic commands for robot_kit"""

    """Test for the NeoPixelStrip class"""
    led_strip = NeoPixelStrip()

    # Turn the LEDs Yellow and then Green
    led_strip.on(128, 128, 0)
    time.sleep(1.0)
    led_strip.on(0, 255, 0)
    time.sleep(1.0)
    led_strip.off()

    # Turn the wheels
    wheels = Wheels()
    wheels.all(0.25)
    time.sleep(1.0)
    wheels.stop()
```
