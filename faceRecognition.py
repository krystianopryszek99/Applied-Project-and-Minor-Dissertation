import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os
import database
import csv

def runRecognition():
    path = 'download'
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
    print("List of all people found:")
    print(classNames)

    # function that will compute all the encodings
    def getEncodings(images):
        print("Getting all the encodings...")
        # list with all encodings
        encodeList = []
        # looping through all images
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # finding the encodings
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    # function to clock in
    def checkIn(name):
        # csv header
        fieldnames = ['Student','Time', 'Date']

        #write to csv file code here
        with open('clockingLog/Logs.csv', 'a', newline = '') as f:
            # list of names
            nameList = []
            # if name is not present in the list
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if name not in nameList:
                currentTime = datetime.now()
                timeString = currentTime.strftime('%H:%M:%S')
                dateString = currentTime.strftime('%d/%m/%Y')
                if os.stat('clockingLog/Logs.csv').st_size == 0:
                    writer.writeheader()
                writer.writerow({
                    'Student' : name,
                    'Time' : timeString,
                    'Date' : dateString,
                })

    # This function will get all faces that it knows 
    getEncodeList = getEncodings(images)
    print('Found Encodings')

    # initialising webcam
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) 

    # while loop to get each frame one by one 
    while True:
        success, img = cap.read()
        resizedImg = cv2.resize(img,(0,0),None,0.25,0.25)
        # convert into rgb
        resizedImg = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2RGB)
        
        # find location of the faces
        facesCurrentFrame = face_recognition.face_locations(resizedImg)
        encodesCurrentFrame = face_recognition.face_encodings(resizedImg,facesCurrentFrame)

        # finding the matches
        # using zip as it allows you to iterate two lists at the same time
        for encodeFace,faceLocation in zip(encodesCurrentFrame,facesCurrentFrame):
            # matching, compares the list of faces that it knows and one of the encodings
            matches = face_recognition.compare_faces(getEncodeList,encodeFace)
            # find distance 
            faceDistance = face_recognition.face_distance(getEncodeList,encodeFace)
            print(faceDistance)
            matchIndex = np.argmin(faceDistance)
            
            if matches[matchIndex]:
                # show name of the best match
                name = classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLocation
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(255,0,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                # if the matches a face it will automatically close the program after 3 seconds
                if matches[matchIndex] == True:
                    # Display the resulting frame
                    cv2.imshow('Image Capturing',img)
                    # check in 
                    print(name + " has checked In!")
                    checkIn(name)
                    # Delete the image of the downloads folder after it has been retrieved from the database.
                    #path = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/download/" + name + ".jpg"
                    #os.remove(path)
                    cv2.waitKey(3000)
                    cap.release()
                    # destroys all the windows we created
                    cv2.destroyAllWindows()