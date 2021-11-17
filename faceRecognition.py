import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os

def runRecognition():
    path = 'images'
    # list of images
    images = []
    # names of images
    classNames = []
    myList = os.listdir(path)
    # use the names of images and import them 
    for element in myList:
        currentImg = cv2.imread(f'{path}/{element}')
        # append currentImg
        images.append(currentImg)
        # append classNames
        classNames.append(os.path.splitext(element)[0])
    print("List of all images found:")
    print(classNames)