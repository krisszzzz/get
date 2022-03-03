import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

number = [0, 0, 1, 0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, number)


time.sleep(15)


GPIO.output(dac, 0)

GPIO.cleanup()


#x;y1;
#256;3.23;
#127;1.653;
#64; 0.853;
#32; 0.499;
#5;  0.48;
#0;  0.42;
#256; 0.42;