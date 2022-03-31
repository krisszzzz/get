
import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def adc():
    value = 0
    for i in range(7, -1, -1):
        step = 2**i
        value += step
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.005)

        if GPIO.input(comp) == 0:
            value -= step

    print("ADC decimal = {}".format(value))
    return value



try:
    while True:
        print("voltage is ", "{:.2f}".format(adc() / 256 * 3,3))

finally:
        GPIO.output(dac, 0)
        GPIO.output(troyka, 0)
        GPIO.cleanup()
        


