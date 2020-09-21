"""A lightweight wrapper around the NeoPixel LED Strip"""
import board
import neopixel


class NeoPixelStrip():
    """A lightweight wrapper around the NeoPixel LED Strip
       Usage:
            led_strip = NeoPixelStrip()
            led_strip.on(255, 0, 0)  # R, G, B
            time.sleep(1)
            led_strip.off()
    """
    def __init__(self, led_pin=board.D18, num_leds=8, brightness=1.0):
        """NeoPixelStrip Initialization"""
        self.led_pin = led_pin
        self.num_leds = num_leds
        self.brightness = brightness
        self.strip = neopixel.NeoPixel(self.led_pin, self.num_leds, brightness=self.brightness)

    def on(self, red, green, blue):
        """Turn all the LEDs to one color
        Args:
               red: red value (0-255)
               green: green value (0-255)
               blue: blue value (0-255)
        """
        self.strip.fill((red, green, blue))

    def off(self):
        """Turn all the LEDs off"""
        self.strip.fill((0, 0, 0))

    def cleanup(self):
        """Method that's called when class is destroyed"""
        print('Cleanup...')
        self.off()
        self.strip.deinit()


def test():
    """Test for the NeoPixelStrip class"""
    import time
    led_strip = NeoPixelStrip()
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

    led_strip.off()
    led_strip.cleanup()


if __name__ == '__main__':

    # Run the test
    test()
