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
    window = tk.Tk()
    window.geometry("500x400")
    window.resizable(True,False)
    window.title("Registration")

    # Register Frame
    Register_Frame=Frame(window,bd=4,relief=RIDGE, bg="blue")
    Register_Frame.place(x=0, y=0, width=500, height=400)

    reg_title=Label(Register_Frame, text="Registration",font=("times new roman", 30, "bold"),bg="blue", fg="white")
    reg_title.grid(row=0, columnspan=2, pady=10)

    text = Label(Register_Frame, text="Click 'Capture' to take a picture of your face \n Hit 'S' to save the image OR 'Q' to close the program",font=("times new roman", 15, "bold"),bg="blue", fg="white")
    text.place(x=0,y=90)

    # Button 
    RegButton = tk.Button(Register_Frame, text="Capture", command=captureImg, fg="black"  ,bg="white"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    RegButton.place(x=10, y=180)

    window.mainloop()

def captureImg():
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
        # click 'q' to close the program
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        if k % 256 == 27:
            print("Program closing..")
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()
        # click 's' to save the image
        #elif cv2.waitKey(1) & 0xFF == ord('s'):
        elif k % 256 == 32:
            # for now it's hardcoded, will be changed for manually entering employee name 
            img_name = "images/krystian2.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            #mongoConn()
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

# Buttons 
clockInButton = tk.Button(Left_Frame, text="Clock In/Out", command=facialRecognition ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
clockInButton.place(x=100, y=100)

ExitButton = tk.Button(Left_Frame, text="Exit", command=closeProgram ,fg="white"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
ExitButton.place(x=100, y=230)

# entry 

lbl_name = Label(Right_Frame, text="Name", bg="white",fg="black",font=('times', 20, ' bold '))
lbl_name.place(x=100, y=100)

txt_name=Entry(Right_Frame,textvariable=name, font=('times', 20, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=100, y=150)

RegButton = tk.Button(Right_Frame, text="Register", command=captureImg ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
RegButton.place(x=100, y=230)

#

window.mainloop()