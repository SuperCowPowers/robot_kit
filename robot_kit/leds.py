"""A lightweight wrapper around the NeoPixel LED Strip"""
import board
import neopixel
import time


class NeoPixelStrip():
    """A lightweight wrapper around the NeoPixel LED Strip
       Usage:
            led_strip = NeoPixelStrip()
            led_strip.on(255, 0, 0)  # R, G, B
            time.sleep(1)
            led_strip.off()
    """
    # Singleton Object Pattern
    __instance = None

    def __new__(cls, led_pin=board.D18, num_leds=8, brightness=1.0):
        if NeoPixelStrip.__instance is None:
            NeoPixelStrip.__instance = object.__new__(cls)
            NeoPixelStrip.__instance.__class_init__(led_pin, num_leds, brightness)
        return NeoPixelStrip.__instance

    @classmethod
    def __class_init__(cls, led_pin=board.D18, num_leds=8, brightness=1.0):
        """NeoPixelStrip Initialization"""
        cls.led_pin = led_pin
        cls.num_leds = num_leds
        cls.brightness = brightness
        cls.strip = neopixel.NeoPixel(cls.led_pin, cls.num_leds, brightness=cls.brightness)

    def __init__(self):
        self.current_rgb = (0, 0, 0)

    def get_rgb(self):
        """Return the current color of the LEDs"""
        return self.current_rgb[0], self.current_rgb[1], self.current_rgb[2]

    def on(self, red, green, blue):
        """Turn all the LEDs to one color
        Args:
               red: red value (0-255)
               green: green value (0-255)
               blue: blue value (0-255)
        """
        self.strip.fill((red, green, blue))
        self.current_rgb = (red, green, blue)

    def off(self):
        """Turn all the LEDs off"""
        self.strip.fill((0, 0, 0))

    def cleanup(self):
        """Method that's called when class is destroyed"""
        print('Cleanup...')
        self.off()
        self.strip.deinit()


class CommandBlink:

    def __init__(self, function):
        self.led_strip = NeoPixelStrip()
        self.function = function

    def __call__(self, *args, **kwargs):
        # Turn LEDs blue
        self.led_strip.on(0, 0, 255)

        # Call the function
        self.function(*args, **kwargs)

        # Turn LEDs Off
        time.sleep(0.1)  # Quick sleep in case function didn't take long
        self.led_strip.off()


def test():
    """Test for the NeoPixelStrip class"""

    # Create the class
    led_strip = NeoPixelStrip()

    # Test the CommandBlink Decorator
    @CommandBlink
    def foo(a):
        print(a)
    foo(0.5)
    time.sleep(1.0)

    for r, g, b in zip(range(128, 0, -1), range(0, 128), range(0, 128)):
        led_strip.on(r, g, b)
        time.sleep(0.01)

    # Yellow
    led_strip.on(128, 128, 0)
    time.sleep(1.0)

    # Orange
    led_strip.on(255, 128, 0)
    time.sleep(1.0)

    # Red
    led_strip.on(255, 0, 0)
    time.sleep(1.0)

    # Green
    led_strip.on(0, 255, 0)
    time.sleep(1.0)

    # Turn off led strip
    led_strip.off()
    led_strip.cleanup()


if __name__ == '__main__':

    # Run the test
    test()
