
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
    for i in range(0, 255):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.005)
        input = GPIO.input(comp)

        if input == 0:
            print("ADC decimal = {}".format(i))
            return i



try:
    while True:
        print("voltage is ", "{:.2f}".format((adc() / 256) * 3,3))

finally:
        GPIO.output(dac, 0)
        GPIO.output(troyka, 0)
        GPIO.cleanup()
        


