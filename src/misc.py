import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep



driver_motor_running = False
drive_mode = "Forward"

steer = "Left"
steering_mode = False

def bootUp():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) 
    GPIO.cleanup()
    #gpio for motor drivers

    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)   #motor 1 forward
    GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)   #motor 1 reverse
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)   #motor 2 forward
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   #motor 2 reverse


    #steering
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

    #start PWM running, but with value of 0 (pulse off)
    servo1.start(7)


def isCentered(w,h,origin_x,origin_y,width,height):
    midw = w/2
    midh = h/2
    tolerance = 100 #each side
    mid_x = origin_x + width//2
    #mid_y = origin_y + height//2
    if(abs(midw - mid_x) <= tolerance):
        print(True,abs(midw - mid_x))
    else:
        print(False,abs(midw - mid_x))

def getArea(w,h):
    area = w*h
    print(area)

def motorDriver():
    global driver_motor_running,drive_mode
    while True: 
        if(driver_motor_running):
            if(drive_mode == "Forward"):
                GPIO.output(3,GPIO.HIGH)
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(5,GPIO.LOW)
                GPIO.output(8,GPIO.LOW)
            elif(drive_mode == "Reverse"):
                GPIO.output(3,GPIO.LOW)
                GPIO.output(7,GPIO.LOW)
                GPIO.output(5,GPIO.HIGH)
                GPIO.output(8,GPIO.HIGH)
            else:
                pass
        else:
            GPIO.cleanup()

def steering():
    global steering,steering_mode
    if steering_mode:
        if steer == "Left":
            pass

