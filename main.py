# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from tkinter import messagebox

from time import strftime
import cv2
import faceRecognition
import os
import mongoStore

def time():
    # Time and date
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    label.config(text=string)
    label.after(1000, time)

def facialRecognition():
    show_checkInMenu()
    faceRecognition.runRecognition()

def storeUser():
    mongoStore.store()

def alreadyCheckedIn():
    messagebox.showerror("Alert","You are already checked In!")

def register():
    # if message box is empty, displays alert.
    if len(txt_name.get()) == 0:
        messagebox.showerror("Alert","Please enter your name")
    else:
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
                # store user to database
                storeUser()
                # Delete the image of the images folder after it has been stored on the database.
                path = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/images/" + name.get() + ".jpg"
                os.remove(path)
                img_counter += 1
                # closes the webcam
                cap.release()
                # destroys all the windows we created
                cv2.destroyAllWindows()
                # After registration, redirect to main menu
                show_mainMenuFrame()

def closeProgram():
    os._exit(0)

# User Interface (Main Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Clocking Management System")   

# Stores the name when registering 
name = tk.StringVar()

def show_mainMenuFrame():
    regMenuFrame.grid_forget()
    mainMenuFrame.grid()

def show_regMenu():
    mainMenuFrame.grid_forget()
    checkedInMenuFrame.grid_forget()
    regMenuFrame.grid()

def show_checkInMenu():
    mainMenuFrame.grid_forget()
    regMenuFrame.grid_forget()
    checkedInMenuFrame.grid()

def show_healthCheckMenu():
    mainMenuFrame.grid_forget()
    regMenuFrame.grid_forget()
    healthMenuFrame.grid()

# Main Menu Frame

mainMenuFrame = Frame(window)

label=Label(mainMenuFrame, font=("times new roman", 30, "bold"),bg="grey", fg="white")
label.grid(row=0, column=0, sticky="nsew")
time()  

Frame(mainMenuFrame).grid(row=1, column=0, padx=514, pady=500)

# Left Frame
Left_Frame=Frame(mainMenuFrame,bd=4,relief=RIDGE, bg="white")
Left_Frame.place(x=0, y=95, width=520, height=425)

# Right Frame
Right_Frame=Frame(mainMenuFrame,bd=4,relief=RIDGE, bg="white")
Right_Frame.place(x=510, y=95, width=520, height=425)

lbl=Label(Left_Frame, font=("times new roman", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
alreadyReg_title = Label(Left_Frame, text="Already Registered", bg="blue", fg="white", font=('times new roman', 20, ' bold '))
alreadyReg_title.place(x=140, y=10)

lbl=Label(Right_Frame, font=("times new roman", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
newUsers_title = Label(Right_Frame, text="New Users", bg="blue", fg="white", font=('times new roman', 20, ' bold '))
newUsers_title.place(x=180, y=10)

# Buttons 
clockInButton = tk.Button(Left_Frame, text="Check In", command=facialRecognition, fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
clockInButton.place(x=100, y=100)

ExitButton = tk.Button(Left_Frame, text="Exit", command=closeProgram, fg="white" ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
ExitButton.place(x=100, y=230)

RegButton = tk.Button(Right_Frame, text="Register", command=show_regMenu ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('times new roman', 30, ' bold '))
RegButton.place(x=100, y=170)

# Registration Menu Frame

regMenuFrame = Frame(window, bg="#447c84")

Frame(regMenuFrame).grid(row=1, column=0, padx=514, pady=500)

# Reg Frame
Reg_Frame=Frame(regMenuFrame,bd=4,relief=RIDGE, bg="white")
Reg_Frame.place(x=300, y=95, width=400, height=400)

lbl_name = Label(Reg_Frame, text="Name", bg="white",fg="black",font=('times new roman', 20, ' bold '))
lbl_name.place(x=50, y=50)

txt_name=Entry(Reg_Frame,textvariable=name, font=('times new roman', 20, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=50, y=100)

# Buttons 
RegButton = tk.Button(Reg_Frame, text="Submit", command=register ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times new roman', 20, ' bold '))
RegButton.place(x=100, y=200)

BackButton = tk.Button(Reg_Frame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('times new roman', 15, ' bold '))
BackButton.place(x=10, y=330)

# Checked-in menu frame

checkedInMenuFrame = Frame(window)

label=Label(checkedInMenuFrame, font=("times new roman", 30, "bold"), bg="grey", fg="white")
label.grid(row=0, column=0, sticky="nsew")
time()  

Frame(checkedInMenuFrame).grid(row=1, column=0, padx=514, pady=500)

# Left Frame
Left_Frame=Frame(checkedInMenuFrame,bd=4, relief=RIDGE, bg="white")
Left_Frame.place(x=0, y=95, width=520, height=425)

# Right Frame
Right_Frame=Frame(checkedInMenuFrame,bd=4, relief=RIDGE, bg="white")
Right_Frame.place(x=510, y=95, width=520, height=425)

lbl=Label(Left_Frame, font=("times new roman", 40, "bold"),bg="green", fg="white")
lbl.pack(side=TOP, fill=X)
alreadyReg_title = Label(Left_Frame, text="Already Registered", bg="green", fg="white", font=('times new roman', 20, ' bold '))
alreadyReg_title.place(x=140, y=10)

lbl=Label(Right_Frame, font=("times new roman", 40, "bold"),bg="green", fg="white")
lbl.pack(side=TOP, fill=X)
newUsers_title = Label(Right_Frame, text="New Users", bg="green", fg="white", font=('times new roman', 20, ' bold '))
newUsers_title.place(x=180, y=10)

# Buttons for checked-in menu
clockInButton = tk.Button(Left_Frame, text="Check In", command=alreadyCheckedIn, fg="white"  ,bg="green"  ,width=11 ,activebackground="white" ,font=('times new roman', 30, ' bold '))
clockInButton.place(x=100, y=100)

ExitButton = tk.Button(Left_Frame, text="Exit", command=closeProgram, fg="white" ,bg="red"  ,width=11 ,activebackground="white" ,font=('times new roman', 30, ' bold '))
ExitButton.place(x=100, y=230)

RegButton = tk.Button(Right_Frame, text="Register", command=show_regMenu ,fg="white"  ,bg="blue"  ,width=11 ,activebackground="white" ,font=('times new roman', 30, ' bold '))
RegButton.place(x=100, y=170)

# Health Check Form Menu

healthMenuFrame = Frame(window, bg="yellow")

Frame(healthMenuFrame).grid(row=1, column=0, padx=514, pady=500)

# HealthCheck Frame
HealthCheck_Frame=Frame(healthMenuFrame,bd=4,relief=RIDGE, bg="white")
HealthCheck_Frame.place(x=300, y=25, width=500, height=480)

mobile_label = Label(HealthCheck_Frame,text = "Mobile Number : ", bg="white",fg="black",font=('times new roman', 10, ' bold '))
mobile_label.place(x=0, y=10)

college_label = Label(HealthCheck_Frame,text = "College attending : ", bg="white",fg="black",font=('times new roman', 10, ' bold '))
college_label.place(x=0, y=30)

text_label = Label(HealthCheck_Frame,text = "if you have any symptoms of COVID-19 (coronavirus) self-isolate (stay in your room)\n - Email Covidofficer@gmit.ie\n The most common symptoms of COVID-19 are:\n •fever (high temperature - 38 degrees Celsius or above) - including having chills\n •dry cough\n •fatigue (tiredness)\n Confirming: • I am not awaiting results of a COVID-19 test.\n • I have not been diagnosed with, confirmed or suspected of COVID-19 in the past 14 days.\n Click YES to confirm I AM SYMPTOM FREE, AND I AM ATTENDING CAMPUS FOR\n WORK /STUDY/VISIT TODAY\n ", bg="white",fg="black",font=('times new roman', 10, ' bold '))
text_label.place(x=0, y=250)

# user input 

# name entry
mobile_var = tk.StringVar()
mobile_entry = Entry(HealthCheck_Frame, width = 20, textvariable = mobile_var)
mobile_entry.place(x=100, y=10)
mobile_entry.focus()

# Radio Buttons - List of colleges
college_attend = tk.StringVar()
radiobtn1 = Radiobutton(HealthCheck_Frame, text = 'Dublin Road Campus, Galway', value='Dublin Road Campus, Galway', bg="white",fg="black", variable = college_attend)
radiobtn1.place(x=150, y=30)

radiobtn2 = Radiobutton(HealthCheck_Frame, text = 'Mayo Campus, Castlebar', value='Mayo Campus, Castlebar', bg="white",fg="black",variable = college_attend)
radiobtn2.place(x=150, y=60)

radiobtn3 = Radiobutton(HealthCheck_Frame, text = 'CCAM, Cluain Mhuire, Galway', value='CCAM, Cluain Mhuire, Galway', bg="white",fg="black", variable = college_attend)
radiobtn3.place(x=150, y=90)

radiobtn4 = Radiobutton(HealthCheck_Frame, text = 'All Core Gym, Ballybrit', value='All Core Gym, Ballybrit', bg="white",fg="black",variable = college_attend)
radiobtn4.place(x=150, y=120)

radiobtn5 = Radiobutton(HealthCheck_Frame, text = 'Mountbellew Campus, County Galway', value='Mountbellew Campus, County Galway', bg="white",fg="black",variable = college_attend)
radiobtn5.place(x=150, y=150)

radiobtn6 = Radiobutton(HealthCheck_Frame, text = 'Letterfrack, County Galway', value='Letterfrack, County Galway', bg="white",fg="black",variable = college_attend)
radiobtn6.place(x=150, y=180)

radiobtn7 = Radiobutton(HealthCheck_Frame, text = 'GMIT (Organised Field Trip)', value='GMIT (Organised Field Trip)', bg="white",fg="black",variable = college_attend)
radiobtn7.place(x=150, y=210)

# Confirmation
confirmation = tk.StringVar()
radiobtn8 = Radiobutton(HealthCheck_Frame, text = 'Yes', value='Yes', bg="white",fg="black",variable = confirmation)
radiobtn8.place(x=0, y=400)

# submit form button
submit_button = Button(HealthCheck_Frame, text = "Submit")  
submit_button.place(x=200, y=420)

mainMenuFrame.grid()

window.mainloop()