import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)


#while True:
    #print(GPIO.input(15))
GPIO.output(14, GPIO.input(15))