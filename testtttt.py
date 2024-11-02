# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(7)
servo1.ChangeDutyCycle(4.5)
time.sleep(1)
servo1.ChangeDutyCycle(9.5)
time.sleep(1)
servo1.ChangeDutyCycle(7)
time.sleep(1)

servo1.stop()
GPIO.cleanup()
