import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep



driver_motor_running = False
drive_mode = "Forward"

steer = False
steering_mode = "Straight"


#GPIO.cleanup()   
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 


class arm:
    def __init__(self):
        #base
        GPIO.setup(11,GPIO.OUT)   
        self.base_servo = GPIO.PWM(11,50)
        self.base_servo.start(2)
        sleep(1)
        #shoulder
        GPIO.setup(12,GPIO.OUT)
        self.shoulder_servo = GPIO.PWM(12,50)
        self.shoulder_servo.start(3)
        sleep(1)
        #elbow
        GPIO.setup(13,GPIO.OUT)   
        self.elbow_servo = GPIO.PWM(13,50)
        self.elbow_servo.start(4)
        sleep(1)
        #wrist_horizonal
        GPIO.setup(15,GPIO.OUT)
        self.wrist_horizontal = GPIO.PWM(15,50)
        self.wrist_horizontal.start(2)
        sleep(1)
        #wrist_vertical
        GPIO.setup(16,GPIO.OUT)
        self.wrist_vertical = GPIO.PWM(16,50)
        self.wrist_vertical.start(2)
        sleep(1)
        #fingers
        GPIO.setup(18,GPIO.OUT)
        self.finger_servo = GPIO.PWM(18,50)
        self.finger_servo.start(7)
        sleep(1)
    def base(self,angle):
        self.base_servo.ChangeDutyCycle(angle)
        sleep(1)
    def shoulder(self,angle):
        self.shoulder_servo.ChangeDutyCycle(angle)
        sleep(1)
    def elbow(self,angle):
        self.elbow_servo.ChangeDutyCycle(angle)
        sleep(1)
    def wrist_h(self,angle):
        self.wrist_horizontal.ChangeDutyCycle(angle)
        sleep(1)
    def wrist_v(self,angle):
        self.wrist_vertical.ChangeDutyCycle(angle)
        sleep(1)
    def fingers(self,angle):
        self.finger_servo.ChangeDutyCycle(angle)
        sleep(1)
arm1 = arm()



def isCentered(w,origin_x,width):
    midw = w/2
    tolerance = 25 #each side
    mid_x = (origin_x+(width/2))
    #mid_y = origin_y + height//2
    if(midw - mid_x > tolerance):
        return "Left"
    elif ((midw - mid_x) < (-1*tolerance)):
        return "Right"
    else:
        return "Straight"

def getArea(w,h):
    area = w*h
    return area

def motrDriver():
    global driver_motor_running,drive_mode
    GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)   #motor 1 forward
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)   #motor 1 reverse
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)   #motor 2 forward
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)   #motor 2 reverse
    while True:
        if driver_motor_running:
            if drive_mode == "Forward":
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(22,GPIO.HIGH)
                GPIO.output(21,GPIO.LOW)
                GPIO.output(23,GPIO.LOW)
            else:
                GPIO.output(19,GPIO.LOW)
                GPIO.output(22,GPIO.LOW)
                GPIO.output(21,GPIO.HIGH)
                GPIO.output(23,GPIO.HIGH)
        else:
            GPIO.output(19,GPIO.LOW)
            GPIO.output(22,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)

def steering():
    global steer,steering_mode
    GPIO.setup(24,GPIO.OUT)
    steering_servo = GPIO.PWM(24,50)
    steering_servo.start(7)
    while True:
        if steer:
            if steering_mode == "Left":
                steering_servo.ChangeDutyCycle(9)
                sleep(1)
            elif steering_mode == "Straight":
                steering_servo.ChangeDutyCycle(7)
                sleep(0.5)
            else:
                steering_servo.ChangeDutyCycle(5)
                sleep(0.5)

