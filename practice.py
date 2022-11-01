import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamoff()
me.streamon()
me.takeoff()
me.send_rc_control(0, 0, 25, 0)
time.sleep(2.2)

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0
flag = True

def move():
    me.streamoff()
    me.streamon()
    me.takeoff()

    me.move_back(20)
    me.move_forward(20)

    me.move_back(20)
    me.move_forward(20)

    me.move_back(20)
    me.move_forward(20)
    
    me.move_back(20)
    me.move_forward(20)

    me.move_back(20)
    me.move_forward(20)

while True:
    #_, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    #print("Center", info[0], "Area", info[1])

    if(flag): move()
    flag = False
    
    cv2.imshow("Output", img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        me.land()
        break