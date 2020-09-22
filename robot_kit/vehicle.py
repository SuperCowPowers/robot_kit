"""A lightweight wrapper around the four servo motors driven by a PCA9685 chip"""
from robot_kit.wheels import Wheels
import time


class Vehicle:
    """A lightweight wrapper around the four servo motors driven by a PCA9685 chip
       Usage:
            vehicle = Vehicle()

            # General Movement
            vehicle.forward(1.0)  # Go forward at full speed
            vehicle.backward(0.5)  # Go backward at half speed
            vehicle.stop()  # Stop the vehicle
            vehicle.turn_left(1.0)  # Turn left at full speed
            vehicle.turn_right(0.5)  # Turn right at half speed

            # Note: When using a 'low speed' (anything less then 0.3 or so the motors don't
                    seem to respond well. I'm assuming this is because their might be some
                    flaws in the example code that drives the PCA9685/PWM device
    """
    def __init__(self):
        """Vehicle Initialization"""
        self.chip_address = 0x40
        self.wheels = Wheels(address=self.chip_address)

    def forward(self, speed):
        """Move the vehicle forward at the given speed"""
        self.wheels.all(speed)

    def backward(self, speed):
        """Move the vehicle forward at the given speed"""
        self.wheels.all(-speed)

    def stop(self):
        """Stop ALL of the vehicle"""
        self.wheels.all(0.0)

    def turn_left(self, speed):
        """Turn left using alternate directions on vehicle"""
        self.wheels.left_front(-speed)
        self.wheels.left_rear(-speed)
        self.wheels.right_front(speed)
        self.wheels.right_rear(speed)

    def turn_right(self, speed):
        """Turn left using alternate directions on vehicle"""
        self.wheels.left_front(speed)
        self.wheels.left_rear(speed)
        self.wheels.right_front(-speed)
        self.wheels.right_rear(-speed)

    def cleanup(self):
        """Method that's called when class is destroyed"""
        print('Cleanup...')


def test():
    """Test for the Vehicle class"""
    vehicle = Vehicle()
    vehicle.forward(0.5)
    time.sleep(0.5)
    vehicle.backward(0.5)
    time.sleep(0.5)
    vehicle.turn_left(0.5)
    time.sleep(0.5)
    vehicle.turn_right(0.5)
    time.sleep(0.5)
    vehicle.stop()

    vehicle.cleanup()


if __name__ == '__main__':

    # Run the test
    test()
