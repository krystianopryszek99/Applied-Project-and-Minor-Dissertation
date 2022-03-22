# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from time import strftime
import cv2
import face
import emailNotification
import os
import database
import csv
from pymongo import MongoClient

def total_students():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["fs.files"]

    # number of documents in the collection
    totalStudents = collection.count_documents({})

    mobile_label = Label(TotalStudents_Frame,text = "Total registered ", fg="black", bg="lightgrey", font=('Helvetica', 15))
    mobile_label.place(x=120, y=10)

    mobile_label = Label(TotalStudents_Frame, text=totalStudents, fg="black", bg="lightgrey", font=('Helvetica', 20))
    mobile_label.place(x=175, y=70)

    ViewButton = tk.Button(TotalStudents_Frame, text="View", command=show_allStudentsPanel, fg="white" ,bg="grey"  ,width=32 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
    ViewButton.place(x=0, y=150)

def time():
    # Time and date
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    time_label.config(text=string)
    time_label.after(1000, time)

def facialRecognition():
    show_mainMenuFrame()
    face.Face_Match()

def register():
    # if message box is empty, displays alert.
    if len(txt_name.get()) == 0:
        messagebox.showerror("Alert","Please enter your name")
    else:
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

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
                # store user to db
                database.store_retrieve(name)
                # stores email address to the db
                database.store_email(name)
                # sends email 
                emailNotification.sendNotification(name)
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

def password():
    if adminPass.get() == "1972":
        messagebox.showinfo("Alert","ACCESS GRANTED!")
        show_adminPanel()
    else:
        messagebox.showerror("Alert","WRONG PASSWORD!")


# User Interface (Main Menu) 

window = tk.Tk()
window.attributes('-fullscreen',True)
window.resizable(True,False)
window.title("Clocking Management System")      

def show_mainMenuFrame():
    regMenuFrame.grid_forget()
    healthMenuFrame.grid_forget()
    loginFrame.grid_forget()
    adminsFrame.grid_forget()
    mainMenuFrame.grid()

def show_regMenu():
    mainMenuFrame.grid_forget()
    regMenuFrame.grid()

def show_healthCheckMenu():
    mainMenuFrame.grid_forget()
    regMenuFrame.grid_forget()
    healthMenuFrame.grid()

def show_login():
    mainMenuFrame.grid_forget()
    loginFrame.grid()

def show_adminPanel():
    loginFrame.grid_forget()
    mainMenuFrame.grid_forget()
    allStudentsFrame.grid_forget()
    studentLogsFrame.grid_forget()
    healthCheckFrame.grid_forget()
    adminsFrame.grid()

def show_allStudentsPanel():
    loginFrame.grid_forget()
    mainMenuFrame.grid_forget()
    adminsFrame.grid_forget()
    allStudentsFrame.grid()

def show_studentLogsFrame():
    loginFrame.grid_forget()
    mainMenuFrame.grid_forget()
    adminsFrame.grid_forget()
    studentLogsFrame.grid()

def show_healthCheckFrame():
    loginFrame.grid_forget()
    mainMenuFrame.grid_forget()
    adminsFrame.grid_forget()
    healthCheckFrame.grid()

# Main Menu Frame

mainMenuFrame = Frame(window, bg="#447c84", relief=RIDGE)

time_label=Label(mainMenuFrame, font=("Helvetica", 30, "bold"),bg="grey", fg="white")
time_label.grid(row=0, column=0, sticky="nsew")
time()  

adminButton = tk.Button(mainMenuFrame, text="Admin", command=show_login, fg="white"  ,bg="blue"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
adminButton.place(x=1400, y=30)

Frame(mainMenuFrame).grid(row=1, column=0, padx=800, pady=800)

# Left Frame
Left_Frame=Frame(mainMenuFrame,bd=4,relief=RIDGE, bg="white")
Left_Frame.place(x=250, y=200, width=520, height=425)

# Right Frame
Right_Frame=Frame(mainMenuFrame,bd=4,relief=RIDGE, bg="white")
Right_Frame.place(x=760, y=200, width=520, height=425)

lbl=Label(Left_Frame, font=("Helvetica", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
alreadyReg_title = Label(Left_Frame, text="Already Registered", bg="blue", fg="white", font=('Helvetica', 20, ' bold '))
alreadyReg_title.place(x=140, y=10)

lbl=Label(Right_Frame, font=("Helvetica", 40, "bold"),bg="blue", fg="white")
lbl.pack(side=TOP, fill=X)
newUsers_title = Label(Right_Frame, text="New Users", bg="blue", fg="white", font=('Helvetica', 20, ' bold '))
newUsers_title.place(x=180, y=10)

# Buttons 
clockInButton = tk.Button(Left_Frame, text="Check In", command=show_healthCheckMenu, fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 30, ' bold '))
clockInButton.place(x=100, y=170)

ExitButton = tk.Button(mainMenuFrame, text="Exit", command=closeProgram, fg="white" ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ExitButton.place(x=10, y=800)

RegButton = tk.Button(Right_Frame, text="Register", command=show_regMenu ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 30, ' bold '))
RegButton.place(x=100, y=170)

# Log in frame (Admin)

loginFrame = Frame(window, bg="#447c84")

Frame(loginFrame).grid(row=1, column=0, padx=768, pady=800)

# Reg Frame
admin_Frame=Frame(loginFrame,bd=4,relief=RIDGE, bg="white")
admin_Frame.place(x=565, y=200, width=400, height=400)

label=Label(loginFrame, text="\nAdmin Dashboard\n", font=("Helvetica", 30, "bold"),bg="#447c84", fg="black")
label.grid(row=0, column=0, sticky="nsew")

lbl_name = Label(admin_Frame,text="Pin", bg="white",fg="black",font=('Helvetica', 20, ' bold '))
lbl_name.place(x=50, y=40)

adminPass = tk.StringVar()
txt_name=Entry(admin_Frame, show="*", textvariable=adminPass, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=50, y=80)

# Buttons 
loginButton = tk.Button(admin_Frame, text="Log in", command=password ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 20, ' bold '))
loginButton.place(x=90, y=270)

BackButton = tk.Button(loginFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# Admin Panel Frame

adminsFrame = Frame(window, bg="#447c84")

Frame(adminsFrame).grid(row=1, column=0, padx=768, pady=800)

label=Label(adminsFrame, text="\nAdmin Dashboard\n", font=("Helvetica", 30, "bold"),bg="#447c84", fg="black")
label.grid(row=0, column=0, sticky="nsew")

TotalStudents_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalStudents_Frame.place(x=115, y=200, width=400, height=200)

total_students()

TotalLogs_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalLogs_Frame.place(x=570, y=200, width=400, height=200)

TotalForms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalForms_Frame.place(x=1025, y=200, width=400, height=200)

With_No_Symptoms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
With_No_Symptoms_Frame.place(x=315, y=500, width=400, height=200)

With_Symptoms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
With_Symptoms_Frame.place(x=815, y=500, width=400, height=200)

# Buttons 
BackButton = tk.Button(adminsFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# All Students Panel

allStudentsFrame = Frame(window, bg="#447c84")

Frame(allStudentsFrame).grid(row=0, column=0, padx=1500, pady=500)

# Students Left Frame
StudentsLeft_Frame=Frame(allStudentsFrame,bd=4,relief=RIDGE, bg="white")
StudentsLeft_Frame.place(x=250, y=25, width=520, height=800)

# Students Right Frame
StudentsRight_Frame=Frame(allStudentsFrame,bd=4,relief=RIDGE, bg="white")
StudentsRight_Frame.place(x=760, y=25, width=520, height=800)

# Display table with db data for:
# all registred students and their email address.
database.all_students(0, StudentsLeft_Frame)
database.student_details(0, StudentsRight_Frame)

BackButton = tk.Button(allStudentsFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# Student logs Panel

studentLogsFrame = Frame(window, bg="#447c84")

Frame(studentLogsFrame).grid(row=0, column=0, padx=1000, pady=500)

StudentLogs_Frame=Frame(studentLogsFrame,bd=4,relief=RIDGE)
StudentLogs_Frame.place(x=350, y=20, width=800, height=800)

database.student_logs(0, StudentLogs_Frame)

BackButton = tk.Button(studentLogsFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# health check Frame

healthCheckFrame = Frame(window, bg="#447c84")

Frame(healthCheckFrame).grid(row=0, column=0, padx=1000, pady=500)

# HealthCheck Frame
HealthCheck_Frame=Frame(healthCheckFrame,bd=4,relief=RIDGE)
HealthCheck_Frame.place(x=350, y=20, width=800, height=800)

database.health_check(0, HealthCheck_Frame)

BackButton = tk.Button(healthCheckFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# Registration Menu Frame

regMenuFrame = Frame(window, bg="#447c84")

Frame(regMenuFrame).grid(row=1, column=0, padx=768, pady=800)

# Reg Frame
Reg_Frame=Frame(regMenuFrame,bd=4,relief=RIDGE, bg="white")
Reg_Frame.place(x=565, y=200, width=400, height=400)

label=Label(regMenuFrame, text="\nRegistration Form\n________________________", font=("Helvetica", 30, "bold"),bg="#447c84", fg="black")
label.grid(row=0, column=0, sticky="nsew")

lbl_name = Label(Reg_Frame, text="Student ID *", bg="white",fg="black",font=('Helvetica', 15, ' bold '))
lbl_name.place(x=50, y=40)

# Stores the name when registering 
name = tk.StringVar()
txt_name=Entry(Reg_Frame,textvariable=name, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=50, y=70)

# Buttons 
RegButton = tk.Button(Reg_Frame, text="Submit", command=register ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 20, ' bold '))
RegButton.place(x=90, y=280)

BackButton = tk.Button(regMenuFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

# Health Check Form Menu

healthMenuFrame = Frame(window, bg="#447c84")

Frame(healthMenuFrame).grid(row=0, column=0, padx=1000, pady=500)

# HealthCheck Frame
HealthCheck_Frame=Frame(healthMenuFrame,bd=4,relief=RIDGE)
HealthCheck_Frame.place(x=350, y=200, width=800, height=480)

heading_label = Label(HealthCheck_Frame,text="GMIT Daily Health Check 2021\n Please DO NOT attend if you\n have any symptoms listed below",fg="black",bg="yellow",width="500",height="3",font="10")
heading_label.pack()

mobile_label = Label(HealthCheck_Frame,text = "Mobile Number: ",fg="black",font=('Helvetica', 12, ' bold '))
mobile_label.place(x=0, y=90)

college_label = Label(HealthCheck_Frame,text = "Choose the college your attending, from the list: ",fg="black",font=('Helvetica', 12, ' bold '))
college_label.place(x=0, y=120)

info_label = Label(HealthCheck_Frame,text = "if you have any symptoms of COVID-19 self-isolate (stay in your room) - Email Covidofficer@gmit.ie.\n The most common symptoms of COVID-19 are:\n •fever (high temperature - 38 degrees Celsius or above) - including having chills\n •dry cough\n •fatigue (tiredness)\n Confirming: • I am not awaiting results of a COVID-19 test.\n • I have not been diagnosed with, confirmed or suspected of COVID-19 in the past 14 days.\n Click YES to confirm I AM SYMPTOM FREE, AND I AM ATTENDING CAMPUS FOR\n WORK /STUDY/VISIT TODAY\n ",fg="black",font=('Helvetica', 12, ' bold '))
info_label.place(x=10, y=250)

confirm_label = Label(HealthCheck_Frame,text = "Click Here: ",fg="black",font=('Helvetica', 10, ' bold '))
confirm_label.place(x=120, y=430)

# Mobile entry box
mobile_var = tk.StringVar()
mobile_entrybox = Entry(HealthCheck_Frame, width = 30, textvariable = mobile_var)
mobile_entrybox.place(x=130, y=90)
mobile_entrybox.focus()

# Radio button
college_attend = tk.StringVar()
radiobtn1 = ttk.Radiobutton(HealthCheck_Frame, text = 'Dublin Road Campus, Galway', value='Dublin Road Campus, Galway', variable = college_attend)
radiobtn1.place(x=150, y=150)

radiobtn2 = ttk.Radiobutton(HealthCheck_Frame, text = 'Mayo Campus, Castlebar', value='Mayo Campus, Castlebar',variable = college_attend)
radiobtn2.place(x=450, y=120)

radiobtn3 = ttk.Radiobutton(HealthCheck_Frame, text = 'CCAM, Cluain Mhuire, Galway', value='CCAM, Cluain Mhuire, Galway',variable = college_attend)
radiobtn3.place(x=150, y=180)

radiobtn4 = ttk.Radiobutton(HealthCheck_Frame, text = 'All Core Gym, Ballybrit', value='All Core Gym, Ballybrit',variable = college_attend)
radiobtn4.place(x=450, y=150)

radiobtn5 = ttk.Radiobutton(HealthCheck_Frame, text = 'Mountbellew Campus, County Galway', value='Mountbellew Campus, County Galway',variable = college_attend)
radiobtn5.place(x=150, y=210)

radiobtn6 = ttk.Radiobutton(HealthCheck_Frame, text = 'Letterfrack, County Galway', value='Letterfrack, County Galway',variable = college_attend)
radiobtn6.place(x=450, y=180)

radiobtn7 = ttk.Radiobutton(HealthCheck_Frame, text = 'GMIT (Organised Field Trip)', value='GMIT (Organised Field Trip)', variable = college_attend)
radiobtn7.place(x=450, y=210)

# Confirmation
confirmation = tk.StringVar()
radiobtn8 = ttk.Radiobutton(HealthCheck_Frame, text = 'YES', value='Yes', variable = confirmation)
radiobtn8.place(x=200, y=430)

# Buttons
BackButton = tk.Button(healthMenuFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=800)

def action():
    mobile = mobile_var.get()
    college = college_attend.get()
    confirm = confirmation.get()

    # csv header
    fieldnames = ['Mobile Number', 'College Attending', 'Confirmation']

    # csv data
    rows = [
        {'Mobile Number' : mobile,
        'College Attending' : college,
        'Confirmation' : confirm}
    ]

    # write to csv file 
    with open('records.csv', 'a', newline = '') as f:
        print("Saving records...")
        # open a file for write only
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # check if size of file is 0
        if os.stat('records.csv').st_size == 0:        
            # write the header
            writer.writeheader()
        # write a row to the csv file
        writer.writerows(rows)
    
    database.store_form(mobile_var, college_attend, confirmation)
    facialRecognition()

# submit form button
submit_button = Button(HealthCheck_Frame, text = "Submit", command = action, font=('Helvetica', 12))  
submit_button.place(x=350, y=430)

mainMenuFrame.grid()

window.mainloop()