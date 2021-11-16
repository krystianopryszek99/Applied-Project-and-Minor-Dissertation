# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from time import strftime
import face

def time():
    string = strftime('%H:%M:%S %p \n %x')
    label.config(text=string)
    label.after(1000, time)

def run():
    face.FaceDetection()

# User Interface (Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Clocking System")   

label=Label(window, font=("times new roman", 30, "bold"),bg="grey", fg="white")
label.pack(side=TOP, fill=X)
time()  

# Left Frame 
Left_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Left_Frame.place(x=0, y=95, width=520, height=460)

# Right Frame
Right_Frame=Frame(window,bd=4,relief=RIDGE, bg="white")
Right_Frame.place(x=510, y=95, width=520, height=460)

# Button
btn_Frame=Frame(Left_Frame, bd=4, bg="white")
btn_Frame.place(x=10, y=100, width=430)

Addbtn=Button(btn_Frame,command=run, text="Run", height=5,width=20).grid(row=0, column=0, padx=5, pady=5)

window.mainloop()