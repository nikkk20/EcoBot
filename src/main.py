import objdetector
import threading
import time
def th1():
    objdetector.main()
th11 = threading.Thread(target=th1)
th11.start()
while True:
    if(len(objdetector.final_result)):
        print(objdetector.final_result)