import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os
import csv
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
from time import strftime
import time

import train_image
import database

class Face_Match: 

    def __init__(self):
        if len(os.listdir('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/download')) == 0:
            messagebox.showerror("Registration","There are no students registred!\nRegister first!")
        else:
            self.path = 'C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/download'
            # list of images
            self.images = []
            # names of images 
            self.imgNames = []
            self.myList = os.listdir(self.path)
            # use the names of images and import them 
            for self.element in self.myList:
                self.currentImg = cv2.imread(f'{self.path}/{self.element}')
                # append currentImg
                self.images.append(self.currentImg)
                # append imgNames
                self.imgNames.append(os.path.splitext(self.element)[0])
            print("List of all people found:")
            print(self.imgNames)

        # This function will get all faces that it knows 
        self.getEncodeList = train_image.getEncodings(self.images)
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
                    # show student ID of the best match
                    self.ID = self.imgNames[self.matchIndex].upper()
                    print(self.ID)
                    y1,x2,y2,x1 = self.faceLocation
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(self.img,(x1,y1),(x2,y2),(255,0,0),2)
                    cv2.rectangle(self.img,(x1,y2-35),(x2,y2),(255,0,0),cv2.FILLED)
                    cv2.putText(self.img,self.ID,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    # if the matches a face it will automatically close the program after 3 seconds
                    if self.matches[self.matchIndex] == True:
                        # Display the resulting frame
                        cv2.imshow('Image Capturing',self.img)
                        # check in 
                        print(self.ID + " has checked In!")
                        checkIn(self.ID)
                        # Delete the image of the downloads folder after it has been retrieved from the database.
                        # After matching known face, program waits for 5 seconds and then closes.
                        cv2.waitKey(3000)
                        self.cap.release()
                        # destroys all the windows we created
                        cv2.destroyAllWindows()
                        checked_menu(self.ID)

# function to clock in
def checkIn(ID):
    # csv header
    fieldnames = ['Student ID','Time', 'Date']

    #write to csv file code here
    with open('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/clockingLog/Logs.csv', 'a', newline = '') as f:
        # list of names
        nameList = []
        # if name is not present in the list
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        if ID not in nameList:
            currentTime = datetime.now()
            timeString = currentTime.strftime('%H:%M:%S')
            dateString = currentTime.strftime('%d/%m/%Y')
            if os.stat('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/clockingLog/Logs.csv').st_size == 0:
                writer.writeheader()
            writer.writerow({
                'Student ID' : ID,
                'Time' : timeString,
                'Date' : dateString,
            })
            database.store_logs(ID, timeString, dateString)

# Checked in menu - displayed when student is successfully matched.
def checked_menu(ID):
    root = Toplevel()
    root.attributes('-fullscreen',True)
    root.resizable(True,False)
    root.title("Clocking Management System")   
    root.configure(bg='#447c84')

    label=Label(root, font=("Helvetica", 30, "bold"),bg="grey", fg="white")
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

    lbl_studentID = Label(Right_Frame, text="Student ID: " +  ID, bg="white",fg="black",font=('Helvetica', 15))
    lbl_studentID.place(x=50, y=60)

    lbl_time = Label(Right_Frame, text="Time: " + strftime("%H:%M:%S"), bg="white",fg="black",font=('Helvetica', 15))
    lbl_time.place(x=50, y=100)

    lbl_date = Label(Right_Frame, text="Date: " + strftime("%d/%m/%Y"), bg="white",fg="black",font=('Helvetica', 15))
    lbl_date.place(x=50, y=140)

    lbl_verify = Label(Right_Frame, text="Verify: " + "Face Recognition", bg="white",fg="black",font=('Helvetica', 15))
    lbl_verify.place(x=50, y=180)

    lbl_info = Label(Right_Frame, text="Successfully verified.", bg="white",fg="black",font=('Helvetica', 15))
    lbl_info.place(x=50, y=220)

    image = Image.open("C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/download/" + ID + ".jpg")
    img = ImageTk.PhotoImage(image)

    lbl_name3 = Label(Left_Frame, image=img)
    lbl_name3.place(x=0, y=0)

    # close after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()