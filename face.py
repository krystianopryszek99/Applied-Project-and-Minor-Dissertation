import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os
import database
import csv
from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
from time import strftime
import time

class Face_Match: 

    def __init__(self):
        self.path = 'download'
        # list of images
        self.images = []
        # names of images
        self.classNames = []
        self.myList = os.listdir(self.path)
        # use the names of images and import them 
        for self.element in self.myList:
            self.currentImg = cv2.imread(f'{self.path}/{self.element}')
            # append currentImg
            self.images.append(self.currentImg)
            # append classNames
            self.classNames.append(os.path.splitext(self.element)[0])
        print("List of all people found:")
        print(self.classNames)

        # function that will compute all the encodings
        def getEncodings(images):
            print("Getting all the encodings...")
            # list with all encodings
            self.encodeList = []
            # looping through all images
            for self.img in images:
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                # finding the encodings
                self.encode = face_recognition.face_encodings(self.img)[0]
                self.encodeList.append(self.encode)
            return self.encodeList

        def storeStudents(name, timeString, dateString):
            database.store_logs(name, timeString, dateString)

        # function to clock in
        def checkIn(name):
            # csv header
            self.fieldnames = ['Student','Time', 'Date']

            #write to csv file code here
            with open('clockingLog/Logs.csv', 'a', newline = '') as f:
                # list of names
                self.nameList = []
                # if name is not present in the list
                self.writer = csv.DictWriter(f, fieldnames = self.fieldnames)
                if name not in self.nameList:
                    self.currentTime = datetime.now()
                    self.timeString = self.currentTime.strftime('%H:%M:%S')
                    self.dateString = self.currentTime.strftime('%d/%m/%Y')
                    if os.stat('clockingLog/Logs.csv').st_size == 0:
                        self.writer.writeheader()
                    self.writer.writerow({
                        'Student' : name,
                        'Time' : self.timeString,
                        'Date' : self.dateString,
                    })
                    storeStudents(name, self.timeString, self.dateString)

        # Checked in menu - displayed when student is successfully matched.
        def checked_menu(name):
            root = Toplevel()
            root.attributes('-fullscreen',True)
            root.resizable(True,False)
            root.title("Clocking Management System")   
            root.configure(bg='#447c84')

            label=Label(root, font=("times new roman", 30, "bold"),bg="grey", fg="white")
            label.pack(side=TOP, fill=X)
            # Time and date
            string = strftime('%H:%M:%S %p \n %d/%m/%Y')
            label.config(text=string)
            label.after(1000, time)

            # Left Frame 
            Left_Frame=Frame(root,bd=4,relief=RIDGE, bg="white")
            Left_Frame.place(x=250, y=200, width=520, height=425)

            # Right Frame
            Right_Frame=Frame(root,bd=4,relief=RIDGE, bg="white")
            Right_Frame.place(x=760, y=200, width=520, height=425)

            lbl_studentID = Label(Right_Frame, text="Student ID: " +  name, bg="white",fg="black",font=('times new roman', 15, ' bold '))
            lbl_studentID.place(x=50, y=60)

            image = Image.open("download/" + name + ".jpg")
            img = ImageTk.PhotoImage(image)

            lbl_name3 = Label(Left_Frame, image=img)
            lbl_name3.place(x=0, y=0)

            root.mainloop()

        # This function will get all faces that it knows 
        self.getEncodeList = getEncodings(self.images)
        print('Found Encodings')

        # initialising webcam
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) 

        # while loop to get each frame one by one 
        while True:
            success, self.img = self.cap.read()
            self.resizedImg = cv2.resize(self.img,(0,0),None,0.25,0.25)
            # convert into rgb
            self.resizedImg = cv2.cvtColor(self.resizedImg, cv2.COLOR_BGR2RGB)
            
            # find location of the faces
            self.facesCurrentFrame = face_recognition.face_locations(self.resizedImg)
            self.encodesCurrentFrame = face_recognition.face_encodings(self.resizedImg,self.facesCurrentFrame)

            # finding the matches
            # using zip as it allows you to iterate two lists at the same time
            for self.encodeFace,self.faceLocation in zip(self.encodesCurrentFrame,self.facesCurrentFrame):
                # matching, compares the list of faces that it knows and one of the encodings
                self.matches = face_recognition.compare_faces(self.getEncodeList,self.encodeFace)
                # find distance 
                self.faceDistance = face_recognition.face_distance(self.getEncodeList,self.encodeFace)
                print(self.faceDistance)
                self.matchIndex = np.argmin(self.faceDistance)
                
                if self.matches[self.matchIndex]:
                    # show name of the best match
                    self.name = self.classNames[self.matchIndex].upper()
                    print(self.name)
                    y1,x2,y2,x1 = self.faceLocation
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(self.img,(x1,y1),(x2,y2),(255,0,0),2)
                    cv2.rectangle(self.img,(x1,y2-35),(x2,y2),(255,0,0),cv2.FILLED)
                    cv2.putText(self.img,self.name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    # if the matches a face it will automatically close the program after 3 seconds
                    if self.matches[self.matchIndex] == True:
                        # Display the resulting frame
                        cv2.imshow('Image Capturing',self.img)
                        # check in 
                        print(self.name + " has checked In!")
                        checkIn(self.name)
                        # Delete the image of the downloads folder after it has been retrieved from the database.
                        #path = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/download/" + name + ".jpg"
                        #os.remove(path)
                        # After matching known face, program waits for 5 seconds and then closes.
                        cv2.waitKey(5000)
                        self.cap.release()
                        # destroys all the windows we created
                        cv2.destroyAllWindows()
                        checked_menu(self.name)