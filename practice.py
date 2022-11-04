import cv2
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamoff()
me.streamon()
me.takeoff()
me.move_up(20)
time.sleep(3.0)
# me.flip('l')
me.flip('r')
#me.flip('b')
me.land()

# image = cv2.imread(r'E:\Dron_termProject\Dron_termProject\picture\profile1.jpg')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

# cv2.imshow('original', image)
# cv2.imshow('gray', gray)
# cv2.imshow('bgr', bgr)
# cv2.imshow('rgb', rgb)
# cv2.waitKey(0)

# import numpy as np
# from djitellopy import tello
# import time

# me = tello.Tello()
# me.connect()
# print(me.get_battery())

# me.streamoff()
# me.streamon()
# me.takeoff()

# me.move_back(20)
# me.move_forward(20)

# me.move_back(20)
# me.move_forward(20)

# me.move_back(20)
# me.move_forward(20)
    
# me.move_back(20)
# me.move_forward(20)

# me.move_back(20)
# me.move_forward(20)

# w, h = 360, 240
# fbRange = [6200, 6800]
# pid = [0.4, 0.4, 0]
# pError = 0
# flag = True

# def move():
#     me.streamoff()
#     me.streamon()
#     me.takeoff()

    # me.move_back(20)
    # me.move_forward(20)

    # me.move_back(20)
    # me.move_forward(20)

    # me.move_back(20)
    # me.move_forward(20)
    
    # me.move_back(20)
    # me.move_forward(20)

    # me.move_back(20)
    # me.move_forward(20)

# while True:
#     #_, img = cap.read()
#     img = me.get_frame_read().frame
#     img = cv2.resize(img, (w, h))
#     #print("Center", info[0], "Area", info[1])

#     if(flag): move()
#     flag = False
    
#     cv2.imshow("Output", img)
#     if cv2.waitkey(1) & 0xFF == ord('q'):
#         me.land()
#         break