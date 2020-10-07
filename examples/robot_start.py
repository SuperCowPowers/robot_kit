"""An example script that uses the functionality of robot_kit"""
from robot_kit.leds import NeoPixelStrip
from robot_kit.wheels import Wheels
from robot_kit.ultrasonic import Ultrasonic
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

    # Get the distance from the Ultrasonic sensor
    dis_sensor = Ultrasonic()
    for i in range(50):
        print(dis_sensor.get_distance())
        time.sleep(0.25)
