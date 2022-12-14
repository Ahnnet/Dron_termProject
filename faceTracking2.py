import cv2
from djitellopy import tello
import time
from datetime import datetime
import random

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamoff()
me.streamon()
me.takeoff()
me.move_up(20)

#????????
w, h = 360, 240
# fbRange = [6200, 6800]
# pid = [0.4, 0.4, 0]
# pError = 0
findcount = 0

# Drons direction predict. -> True: left / False: right
dronDir = True
num = random.randint(0,1)

flagbit = 0

# detect frontal face
def findFace(img):
    faceCascade = cv2.CascadeClassifier("E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []
    detect = False

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        detect = True
        return img, [myFaceListC[i], myFaceListArea[i]], detect
    else:
        return img, [[0, 0], 0], detect

# detect side face
def findSideFace(img):
    faceCascade = cv2.CascadeClassifier("E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_profileface.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        print("left face detected")
        return True
    else:
        print("right face detected")
        return False

# "charm charm charm" motion -> move left and right
def detected():
    me.move_left(20)
    me.move_right(40)
    me.move_left(20)

# plyaer win. -> take commemorative photo
def playerWin():
    print("player Win")
    me.move_up(40)
    me.move_back(60)
    return 0

# dron win. -> annoying player
def dronWin():
    print("drone Win")
    me.flip("b")
    me.move_up(40)
    me.move_down(40)
    me.move_up(40)
    me.move_down(40)
    me.move_up(20)
    me.rotate_clockwise(720)
    return 0

while True:
    #_, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info, detect = findFace(img)

    # if the frontal face detected, findcount++
    if(detect == True): findcount += 1
    
    # after detected
    if(flagbit==1):
        # left
        if(num==1): 
            time.sleep(2.0)
            me.flip('l')
            me.move_right(40)
        # right
        elif(num==0): 
            time.sleep(2.0)
            me.flip('r')
            me.move_left(40)

        print("\n00000000000000000000000000000000000000000000000000000000000000000")
        if(num==1):
            dronDir = True
            print("predict: left")
        else:
            dronDir = False
            print("predict: right")

        # judge the winner
        if(findSideFace(img) == dronDir): 
            dronWin()
        else: 
            playerWin()
            time.sleep(3.0)
            imgSave = me.get_frame_read().frame
        
            now = datetime.now()
            date = str(now.year)+"."+str(now.month)+"."+str(now.day)+"_"+str(now.hour)+"."+str(now.minute)
            path = "E:\Dron_termProject\Dron_termProject\imgs\\"+str(date)+".png"
            # save the file
            cv2.imwrite(path, imgSave)
            print("[INFO] saved")
        print("00000000000000000000000000000000000000000000000000000000000000000")
        
        # finish
        print("judgment finish")
        time.sleep(2.0)
        me.land()
        break

    # face detect stable
    if(findcount==50):
        detected()
        time.sleep(1.0)
        flagbit = 1
        findcount+=1
        
    # terminate
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break