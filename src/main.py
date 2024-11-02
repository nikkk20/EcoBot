import objdetector
import threading
import time
import misc

misc.bootUp()

def th1():
    objdetector.main()
th11 = threading.Thread(target=th1) 
th11.start()

motor_thread = threading.Thread(target=misc.motorDriver)
motor_thread.start()

while True:
    if(len(objdetector.final_result) > 0):
        #print(objdetector.final_result)
        results = objdetector.final_result
        misc.isCentered(640,480,objdetector.final_result[2][0],objdetector.final_result[2][1],objdetector.final_result[2][2],objdetector.final_result[2][3])
        misc.getArea(results[2][2],results[2][3])

# while(True):
#     misc.driver_motor_running = True
#     misc.drive_mode = "Forward"
#     time.sleep(1)
#     misc.drive_mode = "Reverse"
#     time.sleep(1)