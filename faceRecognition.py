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

    # function that will compute all the encodings
    def getEncodings(images):
        # list with all encodings
        encodeList = []
        # looping through all images
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # finding the encodings
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    # function to mark attendance 
    def attendance(name):
        # to open csv file to read and write
        with open('Attendance.csv', 'r+') as f:
            # list 
            myList = f.readlines()
            # list of names
            nameList = []
            for line in myList:
                # find entry and breaks up a string
                entry = line.split(',')
            # if name is not present in the list
            if name not in nameList:
                currentTime = datetime.now()
                timeString = currentTime.strftime('%H:%M:%S')
                dateString = currentTime.strftime('%d/%m/%Y')
                # writes the items of a list to the file 
                f.writelines(f'\n{name},{timeString},{dateString}')

    # This function will get all faces that it knows 
    getEncodeList = getEncodings(images)
    print('Found Encodings')

    # initialising webcam
    cap = cv2.VideoCapture(0)

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
                attendance(name)
        
        # Display the resulting frame
        cv2.imshow('Webcam',img)
        # click 'q' to close the program
        if cv2.waitKey(1000) & 0xFF == ord('s'):
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()
            
