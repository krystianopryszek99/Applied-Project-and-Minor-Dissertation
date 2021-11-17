# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p \n %x')
    label.config(text=string)
    label.after(1000, time)

def register():
    window = tk.Tk()
    window.geometry("500x400")
    window.resizable(True,False)
    window.title("Clocking System")

    # Register Frame
    Register_Frame=Frame(window,bd=4,relief=RIDGE, bg="blue")
    Register_Frame.place(x=0, y=0, width=500, height=400)

    reg_title=Label(Register_Frame, text="Registration",font=("times new roman", 30, "bold"),bg="blue", fg="white")
    reg_title.grid(row=0, columnspan=2, pady=10)

    text = Label(Register_Frame, text="Click 'Capture' to take a picture of your face for registration \n Hit 'Space' to save the image",font=("times new roman", 10, "bold"),bg="blue", fg="white")
    text.place(x=0,y=90)

    # Button 
    RegButton = tk.Button(Register_Frame, text="Capture" ,fg="black"  ,bg="white"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
    RegButton.place(x=10, y=180)

    window.mainloop()

# User Interface (Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Registration")   

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
clockInButton = tk.Button(Left_Frame, text="Clock In" ,fg="white"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
clockInButton.place(x=100, y=100)

clockOutButton = tk.Button(Left_Frame, text="Clock Out",fg="white"  ,bg="red"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
clockOutButton.place(x=100, y=230)

RegButton = tk.Button(Right_Frame, text="Register", command=register ,fg="white"  ,bg="blue"  ,width=11 ,activebackground = "white" ,font=('times', 30, ' bold '))
RegButton.place(x=100, y=160)

window.mainloop()