"""A lightweight wrapper around the four servo motors driven by a PCA9685 chip"""
from robot_kit.PCA9685 import PCA9685
import time


class Wheels:
    """A lightweight wrapper around the four servo motors driven by a PCA9685 chip
       Usage:
            wheels = Wheels()

            # General Movement
            wheels.all(1.0)  # Move all wheels forward at full speed
            wheels.all(-0.5)  # Move all wheels backward at half speed
            wheels.stop()  # Stop all wheels

            # You can also do individual wheels for testing purposes
            wheels.left_front(1.0)  # Turn the left front wheel full speed forward
            wheels.right_rear(-0.5)  # Turn the right rear wheel half speed backward

            # Note: When using a 'low speed' (anything less then 0.3 or so the motors don't
                    seem to respond well. I'm assuming this is because their might be some
                    flaws in the example code that drives the PCA9685/PWM device
    """
    def __init__(self, address=0x40):
        """Wheels Initialization"""
        self.address = address
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)

        # So these channels are taken from example code
        # FIXME: We should find out the logic/why of these channels
        self._wheel_channels = {
                'left_front': [1, 0],
                'left_rear': [2, 3],
                'right_front': [7, 6],
                'right_rear': [5, 4]
                }

    def all(self, speed):
        """Move all of the wheels at the given speed"""
        for wheel in ['left_front', 'left_rear', 'right_front', 'right_rear']:
            self._set_wheel_speed(wheel, speed)

    def stop(self):
        """Stop ALL of the wheels"""
        for wheel in ['left_front', 'left_rear', 'right_front', 'right_rear']:
            self._set_wheel_speed(wheel, 0.0)

    # Note: From this point on are testing methods, in normal operation
    #       you probably shouldn't turn/operation/stop an individual wheel
    def left_front(self, speed):
        """Testing: Turn the left front wheel a certain speed
        Args:
               speed: float (range -1.0 to 1.0)
        """
        self._set_wheel_speed('left_front', speed)

    def left_rear(self, speed):
        """Testing: Turn the left rear wheel a certain speed
        Args:
               speed: float (range -1.0 to 1.0)
        """
        self._set_wheel_speed('left_rear', speed)

    def right_front(self, speed):
        """Testing: Turn the right front wheel a certain speed
        Args:
               speed: float (range -1.0 to 1.0)
        """
        self._set_wheel_speed('right_front', speed)

    def right_rear(self, speed):
        """Testing: Turn the right rear wheel a certain speed
        Args:
               speed: float (range -1.0 to 1.0)
        """
        self._set_wheel_speed('right_rear', speed)

    def test_wheels(self):
        """Testing: A method to test ALL wheels individually"""
        for wheel in ['left_front', 'left_rear', 'right_front', 'right_rear']:
            self.test_wheel(wheel)

    def test_wheel(self, wheel):
        """Helper method to test an individual wheel"""

        # Forward quarter speed and stop
        self._set_wheel_speed(wheel, 0.25)
        time.sleep(0.5)
        self._set_wheel_speed(wheel, 0.0)
        time.sleep(0.5)

        # Backward quarter speed and stop
        self._set_wheel_speed(wheel, -0.25)
        time.sleep(0.5)
        self._set_wheel_speed(wheel, 0.0)
        time.sleep(0.5)

    @staticmethod
    def _convert_range(value):
        """Internal: Convert our -1 to 1 range to the 12bit range of the PWM 'duty'"""

        # Check input range
        if value > 1.0:
            print('Value {:f} clamped to 1.0'.format(value))
            value = 1.0
        if value < -1.0:
            print('Value {:f} clamped to -1.0'.format(value))
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
    wheels = Wheels()
    wheels.test_wheels()

    wheels.all(0.25)
    time.sleep(1.0)
    wheels.stop()
    time.sleep(1.0)

    wheels.cleanup()


if __name__ == '__main__':

    # Run the test
    test()
