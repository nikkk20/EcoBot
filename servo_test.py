# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50) # Note 11 is pin, 50 = 50Hz pulse

GPIO.setup(13,GPIO.OUT)
servo2 = GPIO.PWM(13,50) # Note 11 is pin, 50 = 50Hz pulse
GPIO.setup(15,GPIO.OUT)
servo3 = GPIO.PWM(15,50) # Note 11 is pin, 50 = 50Hz pulse
GPIO.setup(16,GPIO.OUT)
servo4 = GPIO.PWM(16,50) # Note 11 is pin, 50 = 50Hz pulse
GPIO.setup(18,GPIO.OUT)
servo5 = GPIO.PWM(18,50) # Note 11 is pin, 50 = 50Hz pulse

# # #start PWM running, but with value of 0 (pulse off)
servo1.start(5)
time.sleep(1.5)
#servo1.stop()
servo2.start(6.3)
time.sleep(1.5)
servo3.start(2)
time.sleep(1)
servo4.start(4.5)
time.sleep(1)
servo5.start(0)
while 1:
    i = list(map(float,input().split()))
    servo1.ChangeDutyCycle(i[0])
    time.sleep(1)
    servo2.ChangeDutyCycle(i[1])
    time.sleep(1)
    servo3.ChangeDutyCycle(i[2])
    time.sleep(1)
    servo4.ChangeDutyCycle(i[3])
    time.sleep(1)
    servo5.ChangeDutyCycle(i[4])
    time.sleep(1)

# servo2.stop()
# servo3.start(2)
# time.sleep(1.5)
# servo3.stop()
# servo4.start(9)
# time.sleep(1.5)
# servo4.stop()
# servo5.start(9)
# time.sleep(1)

# servo5.stop()
GPIO.cleanup()
