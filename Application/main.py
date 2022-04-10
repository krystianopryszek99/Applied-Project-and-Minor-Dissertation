# Check In System Using Face Recognition

from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from time import strftime
import os
import csv
from threading import Thread
import webbrowser

import database
import capture_image
import face
import emailNotification

class ImageProcessing:
  
    def threading():
        # Allows to run both
        # the capturing of the image and sending an email
        Thread(target = ImageProcessing.captureImage).start()
        Thread(target = ImageProcessing.send_email).start()

    def captureImage():
        filePath = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/download/" + ID.get() + ".jpg"
        if len(txt_name.get()) == 0:
            messagebox.showerror("Alert","Please enter your name")
        elif os.path.exists(filePath):
            messagebox.showerror("Registration","You are already registred!")
            show_mainMenuFrame()
        else:
            capture_image.capture(ID)
            show_mainMenuFrame()
            # store user to db
            database.store_retrieve(ID)
            # stores email address to the db
            database.store_email(ID)
            # Delete the image of the images folder after it has been stored on the database.
            path = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/images/" + ID.get() + ".jpg"
            os.remove(path)

    def send_email():
        # sends email
        emailNotification.sendNotification(ID)

def show_time():
    # Time and date
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    time_label.config(text=string)
    time_label.after(1000, show_time)

def facialRecognition():
    show_mainMenuFrame()
    face.Face_Match()

def closeProgram():
    os._exit(0)

def password():
    if adminPass.get() == "2022":
        messagebox.showinfo("Alert","ACCESS GRANTED!")
        show_adminPanel()
    else:
        messagebox.showerror("Alert","WRONG PASSWORD!")

def delete_by_id():
    database.delete_student(deleteID)
    database.delete_email(deleteID)
    show_adminPanel()

def delete_all():
    messagebox.askquestion("Delete All", "Are you sure?")
    database.delete_all()

def view_chart():
    # open html file
    webbrowser.open('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/stats.html') 

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
show_time()  

adminButton = tk.Button(mainMenuFrame, text="Admin", command=show_login, fg="white"  ,bg="blue"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
adminButton.place(x=150, y=30)

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

ExitButton = tk.Button(mainMenuFrame, text="Exit", command=closeProgram, fg="white" ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ExitButton.place(x=50, y=30)

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
lbl_name.place(x=80, y=40)

adminPass = tk.StringVar()
txt_name=Entry(admin_Frame, show="*", textvariable=adminPass, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=80, y=80)

# Buttons 
loginButton = tk.Button(admin_Frame, text="Sign In", command=password ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 20, ' bold '))
loginButton.place(x=90, y=270)

BackButton = tk.Button(loginFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# Admin Panel Frame

adminsFrame = Frame(window, bg="#447c84")

Frame(adminsFrame).grid(row=1, column=0, padx=768, pady=800)

label=Label(adminsFrame, text="\nAdmin Dashboard\n", font=("Helvetica", 30, "bold"),bg="#447c84", fg="black")
label.grid(row=0, column=0, sticky="nsew")

TotalStudents_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalStudents_Frame.place(x=115, y=150, width=400, height=200)

totalStudents = database.total_students()

totalStudents_label = Label(TotalStudents_Frame,text = "Total registered ", fg="black", bg="lightgrey", font=('Helvetica', 15))
totalStudents_label.place(x=120, y=10)

totalStudentsDocCount_label = Label(TotalStudents_Frame, text=totalStudents, fg="black", bg="lightgrey", font=('Helvetica', 20))
totalStudentsDocCount_label.place(x=175, y=70)

ViewButton = tk.Button(TotalStudents_Frame, text="View", command=show_allStudentsPanel, fg="white" ,bg="grey"  ,width=32 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ViewButton.place(x=0, y=150)

TotalLogs_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalLogs_Frame.place(x=570, y=150, width=400, height=200)

totalCheckins = database.total_checkin()

totalCheckedIn_label = Label(TotalLogs_Frame,text = "Total checked in ", fg="black", bg="lightgrey", font=('Helvetica', 15))
totalCheckedIn_label.place(x=120, y=10)

totalCheckedInDocCount_label = Label(TotalLogs_Frame,text=totalCheckins, fg="black", bg="lightgrey", font=('Helvetica', 20))
totalCheckedInDocCount_label.place(x=175, y=70)

ViewButton = tk.Button(TotalLogs_Frame, text="View", command=show_studentLogsFrame, fg="white" ,bg="grey"  ,width=32 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ViewButton.place(x=0, y=150)

TotalForms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
TotalForms_Frame.place(x=1025, y=150, width=400, height=200)

totalHealthCheckForms = database.total_health_check()

totalForms_label = Label(TotalForms_Frame,text = "Total completed forms ", fg="black", bg="lightgrey", font=('Helvetica', 15))
totalForms_label.place(x=100, y=10)

totalFormsDocCount_label = Label(TotalForms_Frame,text = totalHealthCheckForms, fg="black", bg="lightgrey", font=('Helvetica', 20))
totalFormsDocCount_label.place(x=175, y=70)

ViewButton = tk.Button(TotalForms_Frame, text="View", command=show_healthCheckFrame, fg="white" ,bg="grey"  ,width=32 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ViewButton.place(x=0, y=150)

With_No_Symptoms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
With_No_Symptoms_Frame.place(x=315, y=400, width=400, height=200)

totalSymptomFree = database.total_with_no_symptoms()

totalNoSymptoms_label = Label(With_No_Symptoms_Frame,text = "Total with no symptoms ", fg="black", bg="lightgrey", font=('Helvetica', 15))
totalNoSymptoms_label.place(x=100, y=10)

totalNoSymptomsDocCount_label = Label(With_No_Symptoms_Frame,text = totalSymptomFree, fg="black", bg="lightgrey", font=('Helvetica', 20))
totalNoSymptomsDocCount_label.place(x=175, y=70)

With_Symptoms_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
With_Symptoms_Frame.place(x=815, y=400, width=400, height=200)

totalSymptoms = database.total_with_symptoms()

totalWithSymptoms_label = Label(With_Symptoms_Frame,text = "Total with symptoms ", fg="black", bg="lightgrey", font=('Helvetica', 15))
totalWithSymptoms_label.place(x=100, y=10)

totalWithSymptomsDocCount_label = Label(With_Symptoms_Frame,text = totalSymptoms, fg="black", bg="lightgrey", font=('Helvetica', 20))
totalWithSymptomsDocCount_label.place(x=175, y=70)

# Buttons 

BackButton = tk.Button(adminsFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# Actions Frame for back button, removing all data and to view stats.

Actions_Frame=Frame(adminsFrame,bd=4,relief=FLAT, bg="lightgrey")
Actions_Frame.place(x=550, y=700, width=400, height=50)


RemoveAllButton = tk.Button(Actions_Frame, text="Delete All", command=delete_all ,fg="white"  ,bg="red"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
RemoveAllButton.place(x=0, y=0)

ViewChartButton = tk.Button(Actions_Frame, text="View Statistics", command=view_chart ,fg="white"  ,bg="green"  ,width=15 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
ViewChartButton.place(x=200, y=0)

# All Students Panel

allStudentsFrame = Frame(window, bg="#447c84")

Frame(allStudentsFrame).grid(row=0, column=0, padx=1500, pady=500)

# Students Left Frame
StudentsLeft_Frame=Frame(allStudentsFrame,bd=4,relief=RIDGE, bg="white")
StudentsLeft_Frame.place(x=350, y=25, width=450, height=700)

# Students Right Frame
StudentsRight_Frame=Frame(allStudentsFrame,bd=4,relief=RIDGE, bg="white")
StudentsRight_Frame.place(x=760, y=25, width=450, height=700)

AdminAction_Frame=Frame(allStudentsFrame,bd=4,relief=RIDGE, bg="white")
AdminAction_Frame.place(x=50, y=80, width=260, height=300)

adminTxt_label = Label(AdminAction_Frame,text = "Admin Action\n_____________________", fg="black", bg="white", font=('Helvetica', 15))
adminTxt_label.place(x=10, y=10)

student_label = Label(AdminAction_Frame,text = "Student ID", fg="black", bg="white", font=('Helvetica', 15))
student_label.place(x=10, y=80)

# Deleting student 
deleteID = tk.StringVar()
txt_name=Entry(AdminAction_Frame, textvariable=deleteID, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=10, y=120)

DeleteButton = tk.Button(AdminAction_Frame, text="Delete", command=delete_by_id ,fg="white" ,bg="red"  ,width=10 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
DeleteButton.place(x=10, y=170)

# display data from the db in a table.
student_list = database.all_students(0)

# iterates through the student list,
for i in range(len(student_list)):
    for j in range(len(student_list[0])):
        tbl_txt = tk.Entry(StudentsLeft_Frame, width=300, font=('Helvetica', 10))
        tbl_txt.insert(tk.END,student_list[i][j])
        tbl_txt._values = tbl_txt.get(), i
        tbl_txt.grid(row=i+10, column=j+10)

# display data from the db in a table.
details_list = database.student_details(0)

# iterates through the details list
for i in range(len(details_list)):
    for j in range(len(details_list[0])):
        tbl_txt = tk.Entry(StudentsRight_Frame, width=300, font=('Helvetica', 10))
        tbl_txt.insert(tk.END,details_list[i][j])
        tbl_txt._values = tbl_txt.get(), i
        tbl_txt.grid(row=i+10, column=j+10)

BackButton = tk.Button(allStudentsFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# Student logs Panel

studentLogsFrame = Frame(window, bg="#447c84")

Frame(studentLogsFrame).grid(row=0, column=0, padx=1000, pady=500)

StudentLogs_Frame=Frame(studentLogsFrame,bd=4,relief=RIDGE)
StudentLogs_Frame.place(x=350, y=20, width=800, height=700)

# display data from the db in a table.
logs_list = database.student_logs(0)

# iterates through the logs list
for i in range(len(logs_list)):
    for j in range(len(logs_list[0])):
        tbl_txt = tk.Entry(StudentLogs_Frame, width=40, font=('Helvetica', 10))
        tbl_txt.insert(tk.END,logs_list[i][j])
        tbl_txt._values = tbl_txt.get(), i
        tbl_txt.grid(row=i+10, column=j+10)

BackButton = tk.Button(studentLogsFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# health check Frame

healthCheckFrame = Frame(window, bg="#447c84")

Frame(healthCheckFrame).grid(row=0, column=0, padx=1000, pady=500)

# HealthCheck Frame
HealthCheck_Frame=Frame(healthCheckFrame,bd=4,relief=RIDGE)
HealthCheck_Frame.place(x=350, y=20, width=800, height=700)

# display data from the db in a table.
form_list = database.health_check(0)

# iterates through the form list
for i in range(len(form_list)):
    for j in range(len(form_list[0])):
        tbl_txt = tk.Entry(HealthCheck_Frame, width=40, font=('Helvetica', 10))
        tbl_txt.insert(tk.END,form_list[i][j])
        tbl_txt._values = tbl_txt.get(), i
        tbl_txt.grid(row=i+10, column=j+10)

BackButton = tk.Button(healthCheckFrame, text="Back", command=show_adminPanel ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# Registration Menu Frame

regMenuFrame = Frame(window, bg="#447c84")

Frame(regMenuFrame).grid(row=1, column=0, padx=768, pady=800)

# Reg Frame
Reg_Frame=Frame(regMenuFrame,bd=4,relief=RIDGE, bg="white")
Reg_Frame.place(x=565, y=200, width=400, height=400)

label=Label(regMenuFrame, text="\nRegistration Form", font=("Helvetica", 30, "bold"),bg="#447c84", fg="black")
label.grid(row=0, column=0, sticky="nsew")

lbl_name = Label(Reg_Frame, text="Student ID *", bg="white",fg="black",font=('Helvetica', 15, ' bold '))
lbl_name.place(x=80, y=40)

# Stores the student ID when registering
ID = tk.StringVar() 
txt_name=Entry(Reg_Frame,textvariable=ID, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
txt_name.place(x=80, y=70)

# Buttons 
RegButton = tk.Button(Reg_Frame, text="Submit", command=ImageProcessing.threading ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('Helvetica', 20, ' bold '))
RegButton.place(x=90, y=280)

BackButton = tk.Button(regMenuFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

# Health Check Form Menu

healthMenuFrame = Frame(window, bg="#447c84")

Frame(healthMenuFrame).grid(row=0, column=0, padx=1000, pady=500)

# HealthCheck Frame
HealthCheck_Frame=Frame(healthMenuFrame,bd=4,relief=RIDGE)
HealthCheck_Frame.place(x=350, y=200, width=800, height=520)

heading_label = Label(HealthCheck_Frame,text="GMIT Daily Health Check 2022\n Please DO NOT attend if you\n have any symptoms listed below",fg="black",bg="yellow",width="500",height="3",font="10")
heading_label.pack()

mobile_label = Label(HealthCheck_Frame,text = "Mobile Number: *",fg="black",font=('Helvetica', 12, ' bold '))
mobile_label.place(x=0, y=90)

college_label = Label(HealthCheck_Frame,text = "Choose the college your attending, from the list: *",fg="black",font=('Helvetica', 12, ' bold '))
college_label.place(x=0, y=120)

info_label = Label(HealthCheck_Frame,text = "if you have any symptoms of COVID-19 self-isolate (stay in your room) - Email Covidofficer@gmit.ie.\n The most common symptoms of COVID-19 are:\n •fever (high temperature - 38 degrees Celsius or above) - including having chills\n •dry cough\n •fatigue (tiredness)\n Confirming: • I am not awaiting results of a COVID-19 test.\n • I have not been diagnosed with, confirmed or suspected of COVID-19 in the past 14 days.\n Click YES to confirm I AM SYMPTOM FREE\n OR Click NO to confirm YOU HAVE SYMPTOMS,\n AND I AM ATTENDING CAMPUS FOR WORK /STUDY/VISIT TODAY\n ",fg="black",font=('Helvetica', 12, ' bold '))
info_label.place(x=10, y=250)

confirm_label = Label(HealthCheck_Frame,text = "Click Here: *",fg="black",font=('Helvetica', 10, ' bold '))
confirm_label.place(x=120, y=470)

# Mobile entry box
mobile_var = tk.StringVar()
mobile_entrybox = Entry(HealthCheck_Frame, width = 30, textvariable = mobile_var)
mobile_entrybox.place(x=140, y=90)
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
radiobtn8.place(x=210, y=470)

radiobtn9 = ttk.Radiobutton(HealthCheck_Frame, text = 'NO', value='No', variable = confirmation)
radiobtn9.place(x=250, y=470)

# Buttons
BackButton = tk.Button(healthMenuFrame, text="Back", command=show_mainMenuFrame ,fg="white"  ,bg="red"  ,width=5 ,activebackground = "white" ,font=('Helvetica', 15, ' bold '))
BackButton.place(x=10, y=10)

def on_submit():
    if len(mobile_var.get()) == 0:
        messagebox.showerror("Alert","Please enter your phone number!")
    elif len(college_attend.get()) == 0:
        messagebox.showerror("Alert","Please select college!")
    elif len(confirmation.get()) == 0:
        messagebox.showerror("Alert","Please select your option!")
    else:
        # If the option selected is "No", 
        # It will display alert and won't let anyone check in
        # The form gets stored to the db for
        # breakdown of all records.
        if confirmation.get() == "No":  
            messagebox.showerror("Alert","You have symptoms\nYou are not allowed to check in!")
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
            with open('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/records.csv', 'a', newline = '') as f:
                print("Saving records...")
                # open a file for write only
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                # check if size of file is 0
                if os.stat('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/records.csv').st_size == 0:        
                    # write the header
                    writer.writeheader()
                # write a row to the csv file
                writer.writerows(rows)
            
            # Save the completed form to the db
            database.store_form(mobile_var, college_attend, confirmation)
            show_mainMenuFrame()
            
        # If the selected option is "Yes",
        # It will successfully check in
        # and store it the completed form to the db.
        else:
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
            with open('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/records.csv', 'a', newline = '') as f:
                print("Saving records...")
                # open a file for write only
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                # check if size of file is 0
                if os.stat('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/records.csv').st_size == 0:        
                    # write the header
                    writer.writeheader()
                # write a row to the csv file
                writer.writerows(rows)
            
            # Save the completed form to the db
            database.store_form(mobile_var, college_attend, confirmation)
            # Run the face recogniton
            facialRecognition()

# submit form button
submit_button = Button(HealthCheck_Frame, text = "Submit", command = on_submit, font=('Helvetica', 12))  
submit_button.place(x=350, y=470)

mainMenuFrame.grid()

window.mainloop()