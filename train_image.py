import face_recognition
import cv2
import os

# function that will compute all the encodings
def getEncodings(images):
    print("[INFO] Training images...")
    # list with all encodings
    encodeList = []
    # looping through all images
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # finding the encodings
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        # show all the encoding list
        #print(encodeList)
    return encodeList