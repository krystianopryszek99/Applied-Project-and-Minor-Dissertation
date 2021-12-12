# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from time import strftime
import cv2
import faceRecognition
import os
import mongoConnection

def time():
    # Time and date
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    label.config(text=string)
    label.after(1000, time)

def facialRecognition():
    faceRecognition.runRecognition()

def mongoConn():
    mongoConnection.mongo()

def register():
    cap = cv2.VideoCapture(0)

    img_counter = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("failed")
            break
        cv2.imshow("Registration", frame)

        k = cv2.waitKey(1)
        # click 'esc' to close the program
        if k % 256 == 27:
            print("Program closing..")
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()
        # click 'space' to save the image
        elif k % 256 == 32:
            # saves users name as a image 
            img_name = "images/" + name.get() + ".jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            mongoConn()
            img_counter += 1
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()

def closeProgram():
    os._exit(0)

# User Interface (Main Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Clocking Management System")   

# Stores the name when registering 
name = tk.StringVar()

label=Label(window, font=("times new roman", 30, "bold"),bg="grey", fg="white")
label.pack(side=TOP, fill=X)
time()  

# Left Frame 
Left_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Left_Frame.place(x=0, y=95, width=520, height=425)

# Right Frame
Right_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Right_Frame.place(x=510, y=95, width=520, height=425)

lbl=Label(Left_Frame, font=("times new roman", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
alreadyReg_title = Label(Left_Frame, text="Already Registered", bg="blue", fg="white", font=('times new roman', 20, ' bold '))
alreadyReg_title.place(x=140, y=10)

# Buttons 
clockInButton = tk.Button(Left_Frame, text="Clock In/Out", command=facialRecognition ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
clockInButton.place(x=100, y=100)

ExitButton = tk.Button(Left_Frame, text="Exit", command=closeProgram ,fg="white"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
ExitButton.place(x=100, y=230)

# entry 

lbl=Label(Right_Frame, font=("times new roman", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
newUsers_title = Label(Right_Frame, text="New Users", bg="blue", fg="white", font=('times new roman', 20, ' bold '))
newUsers_title.place(x=180, y=10)

lbl_name = Label(Right_Frame, text="Name", bg="white",fg="black",font=('times new roman', 20, ' bold '))
lbl_name.place(x=100, y=90)

txt_name=Entry(Right_Frame,textvariable=name, font=('times new roman', 20, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=100, y=140)

RegButton = tk.Button(Right_Frame, text="Register", command=register ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
RegButton.place(x=100, y=230)

#

window.mainloop()