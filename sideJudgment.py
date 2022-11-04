import cv2

def judgment(img):
    sideCascade = cv2.CascadeClassifier(r'E:\Dron_termProject\Dron_termProject\opencv-4.x\data\haarcascades\haarcascade_profileface.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = sideCascade.detectMultiScale(imgGray, 1.1, 6)

    # 오른쪽 얼굴
    if(len(faces)==0): return False
    # 왼쪽 얼굴
    else: return True


##########################################
    # myFaceListC = []
    # myFaceListArea = []

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     cx = x + w // 2
    #     cy = y + h // 2
    #     area = w * h
    #     myFaceListArea.append(area)
    #     myFaceListC.append([cx, cy])