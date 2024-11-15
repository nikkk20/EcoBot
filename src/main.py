import objdetector
import threading
import time
import misc

#misc.bootUp()

def th1():
    objdetector.main()
th11 = threading.Thread(target=th1) 
th11.start()
motor_thread = threading.Thread(target=misc.motrDriver)
motor_thread.start()
steering_thread = threading.Thread(target=misc.steering)
steering_thread.start()
# while 1:
    
#     # misc.steer = True
#     # # misc.steering_mode = "Left"
#     # # time.sleep(1)
#     # # misc.steering_mode = "Right"
#     # # time.sleep(1)
#     # misc.steering_mode = "Straight"
#     # time.sleep(1)
#     # misc.steer = False
#     # break

#     # misc.drive_mode = "Forward"
#     # misc.driver_motor_running = True
#     # time.sleep(0.5)

#     misc.drive_mode = "Reverse"
#     misc.driver_motor_running = True
#     time.sleep(0.7)
#     misc.driver_motor_running = False

#     break

# final result = [category,score,[origin_x,origin_y,width,height]]    
mina = 999999999
while True:
    if(len(objdetector.final_result) > 0):
        #print(objdetector.final_result)
        results = objdetector.final_result
        if results[0] == 'bottle':
            
            direction = (misc.isCentered(640,results[2][0],results[2][2]))
            if(direction == "Straight"):
                misc.steering_mode = direction
                misc.steer = True
            else:
                misc.steering_mode = direction
                misc.steer = True
            
            area = misc.getArea(results[2][2],results[2][3])/1000
            print(area)
            if(area<168):
                print("driving")
                misc.drive_mode = "Forward"
                misc.driver_motor_running = True
            else:
                misc.driver_motor_running = False
        else:
            misc.driver_motor_running = False
    else:
        misc.driver_motor_running = False