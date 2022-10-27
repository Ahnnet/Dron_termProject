import cv2
import numpy as np
from matplotlib import pyplot as plt

# load data
# face_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
# side_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')
# eye_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_eye.xml')
########

side_cascade = cv2.CascadeClassifier(r'E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')

##### load object image #####
# image = cv2.imread(r'E:\Dron_termProject\Dron_termProject\picture\profile1.jpg')
image = cv2.imread(r'E:\Dron_termProject\Dron_termProject\picture\side_face9.PNG')


grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

flipped = cv2.flip(grayImage, 1)

##### face cascade #####
scaleFactor = 1.08
minNeighbors = 5
# faces = side_cascade.detectMultiScale(grayImage, scaleFactor, minNeighbors)
faces = side_cascade.detectMultiScale(flipped, scaleFactor, minNeighbors)

if(len(faces)==0): 
    print("No detection!!!!!!!\n\n")

print(faces.shape)
print("faces detected: "+str(faces.shape[0]))
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.rectangle(image, ((0,image.shape[0] -25)), 
              (270, image.shape[0]), (255,255,255), -1)
cv2.putText(image, "test image", (0,image.shape[0] -10), 
            cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)


cv2.namedWindow('RWindow', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RWindow', 400, 600)

##### print image #####

cv2.imshow('RWindow', image)
cv2.waitKey()

# plt.figure(figsize=(12,12))
# plt.imshow(flipped, cmap='gray')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()