"""Ultrasonic Sensor Class"""
import time
import RPi.GPIO as GPIO


class Ultrasonic:
    """Ultrasonic Sensor Class"""
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        self.time_distance_factor = 0.000058  # Time to Centimeters conversion
        self.timeout_distance = 1000  # Distance to return when echo timeout occurs
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        distance_readings = []
        for i in range(5):
            self._send_trigger_pulse()
            pulse_len = self._wait_for_echo()
            # Check for timeout
            if pulse_len == -1:
                return self.timeout_distance
            else:  # Convert pulse time to distance
                distance_readings.append(pulse_len/self.time_distance_factor)
        min_distance = min(distance_readings)
        return min_distance

    def _send_trigger_pulse(self):
        """Internal Method"""
        GPIO.output(self.trigger_pin, 1)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin, 0)

    def _wait_for_echo(self, max_samples=5000):
        """Internal Method"""

        # First we wait for the ON/1 reading (which may timeout)
        for i in range(max_samples):
            if GPIO.input(self.echo_pin) == 1:
                # Now we time how long it takes to get the OFF/0 reading
                start = time.time()
                while GPIO.input(self.echo_pin) != 0:
                    time.sleep(0.00001)  # 10 microseconds
                total_time = time.time() - start
                return total_time

        # Return the Timeout value
        return -1


def test():
    """Test for the Ultrasonic class"""
    import time
    distance_sensor = Ultrasonic()

    # Simply show the distance a bunch of times
    for i in range(50):
        print(distance_sensor.get_distance())
        time.sleep(0.5)


if __name__ == '__main__':

    # Run the test
    test()
