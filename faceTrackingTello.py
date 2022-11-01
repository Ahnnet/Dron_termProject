from utlis import *
import cv2
import time

w, h = 360, 240
pid = [0.4, 0.4, 0]
pError = 0
startCounter = 0  # for no Flight 1   - for flight 0
detectCounter = 0

flag = False

myDrone = initializeTello()

while True:

    ## Flight
    if startCounter == 0:
        myDrone.takeoff()
        myDrone.move_up(20)
        startCounter = 1

    ## Step 1
    img = telloGetFrame(myDrone, w, h)
    ## Step 2
    img, info = findFace(img)

    if(bool(info)==False):
        detectCounter+=1
        print("log: detected!!!!!!!! "+ detectCounter)
    
    if(detectCounter==30):
        myDrone.rotate_clockwise(360)
        time.sleep(1)
        myDrone.rotate_clockwise(360)
        time.sleep(1)
        myDrone.rotate_clockwise(360)
        time.sleep(1)
    

    ## Step 3
    pError = trackFace(myDrone, info, w, pid, pError)
    # print(info[0][0])
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break