import cv2
import numpy as np
from matplotlib import pyplot as plt

# load data
face_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
side_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier(r'.\opencv-4.x\data\haarcascades\haarcascade_eye.xml')

# load object image
image = cv2.imread(r'.\picture\profile1.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# face cascade
faces = face_cascade.detectMultiScale(grayImage, 1.03, 5)

print(faces.shape)
print("faces detected: "+str(faces.shape[0]))
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.rectangle(image, ((0,image.shape[0] -25)), 
              (270, image.shape[0]), (255,255,255), -1)
cv2.putText(image, "test image", (0,image.shape[0] -10), 
            cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

# eye cascade
eyes = eye_cascade.detectMultiScale(grayImage, 1.9, 10)

print(eyes.shape)
print("eyes detected: "+str(eyes.shape[0]))
print(eyes)

for (x,y,w,h) in eyes:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.rectangle(image, ((0,image.shape[0] -25)), 
              (270, image.shape[0]), (255,255,255), -1)
cv2.putText(image, "test image", (0,image.shape[0] -10), 
            cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

# print image
plt.figure(figsize=(12,12))
plt.imshow(image, cmap='gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()