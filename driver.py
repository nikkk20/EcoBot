import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 

#gpio for motor drivers

GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)   #motor 1 forward
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)   #motor 1 reverse
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)   #motor 2 forward
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)   #motor 2 reverse

# GPIO.output(19,GPIO.HIGH)
# GPIO.output(22,GPIO.HIGH)
# GPIO.output(21,GPIO.LOW)
# GPIO.output(23,GPIO.LOW)
# sleep(1)
GPIO.output(19,GPIO.LOW)
GPIO.output(22,GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
sleep(1)
GPIO.cleanup()