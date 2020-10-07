"""Ultrasonic Sensor Class"""
import time
import RPi.GPIO as GPIO


class Ultrasonic:
    """Ultrasonic Sensor Class"""
    def __init__(self):
        GPIO.setwarnings(False)
        self.trigger_pin = 27
        self.echo_pin = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        distance_readings = []
        for i in range(3):
            self._send_trigger_pulse()
            self._wait_for_echo(True, 10000)
            start = time.time()
            self._wait_for_echo(False, 10000)
            finish = time.time()
            pulse_len = finish-start
            distance_readings.append(pulse_len/0.000058)
        avg = sum(distance_readings) / len(distance_readings)
        return avg

    def _send_trigger_pulse(self):
        """Internal Method"""
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00015)
        GPIO.output(self.trigger_pin, False)

    def _wait_for_echo(self, value, timeout):
        """Internal Method"""
        count = timeout
        while GPIO.input(self.echo_pin) != value and count > 0:
            count = count-1


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
