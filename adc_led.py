import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

BITS = 8
LEVELS = 256

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def adc():
    value = 0
    for i in range(7, -1, -1):
        step = 2**i
        value += step
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.01)

        if GPIO.input(comp) == 0:
            value -= step

    print("ADC decimal = {}".format(value))
    return value

def get_bin(value):
    return (1 << int(value * BITS / LEVELS)) - 1 
        

try:
    while True:
        GPIO.output(leds, decimal2binary(get_bin(adc())))
finally:
        GPIO.output(dac, 0)
        GPIO.output(troyka, 0)
        GPIO.cleanup()
        