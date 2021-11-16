import cv2
import numpy as np
from matplotlib import pyplot as plt

def FaceDetection():
    face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('classifiers/haarcascade_eye.xml')

    image = cv2.imread('images/faces.jpg', -1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('Detection',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.show()