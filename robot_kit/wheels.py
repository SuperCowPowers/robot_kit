"""A lightweight wrapper around the four servo motors driven by a PCA9685 chip"""
from PCA9685 import PCA9685


class Wheels():
    """A lightweight wrapper around the four servo motors driven by a PCA9685 chip
       Usage:
            wheels = Wheels()

            # General Movement
            wheels.all(1.0)  # Move all wheels forward at full speed
            wheels.all(-0.5)  # Move all wheels backward at half speed
            wheels.stop()  # Stop all wheels
            wheels.turn_left(45, 0.5)  # Turn left 45 degrees at half speed
            wheels.turn_right(90, 0.1)  # Turn right 90 degrees at slow speed


            # You can also do individual wheels for testing purposes
            wheels.left_front(1.0)  # Turn the left front wheel full speed forward
            wheels.right_back(-0.5)  # Turn the right back wheel half speed backward
    """
    def __init__(self, address=0x40):
        """Wheels Initialization"""
        self.address = address
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)

        # So these channels are taken from example code
        # FIXME: We should find out the logic/why of these channels
        self._wheel_channels = {
                'left_front': [0, 1],
                'left_back': [3, 2],
                'right_front': [6, 7],
                'right_back': [4, 5]
                }

    def left_front(self, speed):
        """Testing: Turn the left front wheel a certain speed
        Args:
               speed: float (range -1.0 to 1.0)
        """
        self._set_wheel_speed('left_front', speed)

    @static_method
    def _convert_range(value):
        """Internal: Convert our -1 to 1 range to the 12bit range of the PWM 'duty'"""

        # Check input range
        if value > 1.0:
            print('Value {:f} clamped to 1.0'.format(value)
            value = 1.0
        if value < 1.0:
            print('Value {:f} clamped to -1.0'.format(value)
            value = -1.0

        # Convert to 12bit (4096-1) range
        return int(value*4095)

    def _set_wheel_speed(self, wheel, speed):
        """Internal: This is an internal method to reduce copy/paste code"""

        # Look up wheel PWM channels
        channels = self._wheel_channels[wheel]

        # Convert speed to duty load
        duty = self._convert_range(speed)

        # Based on positive/negative value of duty we set one channel to 0 and one channel to duty value
        if duty > 0:
            self.pwm.setMotorPwm(channels[0], 0)
            self.pwm.setMotorPwm(channels[1], duty)
        else:
            self.pwm.setMotorPwm(channels[1], 0)
            self.pwm.setMotorPwm(channels[0], abs(duty))

    def cleanup(self):
        """Method that's called when class is destroyed"""
        print('Cleanup...')


def test():
    """Test for the Wheels class"""
    import time
    wheels = Wheels()
    wheels.left_front(0.25)
    time.sleep(1)
    wheels.left_front(0.0)
    wheels.cleanup()


if __name__ == '__main__':

    # Run the test
    test()
