from asyncio.windows_events import NULL
import cv2
import numpy as np

# load data
# face_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
# side_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')
# eye_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_eye.xml')
########
face_cascade = cv2.CascadeClassifier(r'E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
side_cascade = cv2.CascadeClassifier(r'E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier(r'E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_eye.xml')

##### load object image #####
cap = cv2.VideoCapture(r'E:\Dron_termProject\Dron_termProject\picture\frontal_face_video.mp4')

while(True):
    ret,image = cap.read()
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ##### face cascade #####
    faces = face_cascade.detectMultiScale(grayImage, scaleFactor = 1.05, minNeighbors = 5)
    if(len(faces)==0): continue

    print(faces.shape)
    print("faces detected: "+str(faces.shape[0]))
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(image, ((0,image.shape[0] -25)), (270, image.shape[0]), (255,255,255), -1)
        cv2.putText(image, "test image", (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    ##### window size #####
    cv2.namedWindow('RWindow', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('RWindow', 400, 600)


    ##### print image #####

    cv2.imshow('RWindow', image)
    
    if (cv2.waitKey(30)>=0):
        break

