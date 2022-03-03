import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]


GPIO.setmode(GPIO.BCM)


GPIO.setup(leds, GPIO.OUT)

for iter_count in range(3):
    for led_elem in leds:
        GPIO.output(led_elem, 1)
        time.sleep(0.2)
        GPIO.output(led_elem, 0)

GPIO.output(leds, 0)

GPIO.cleanup()


