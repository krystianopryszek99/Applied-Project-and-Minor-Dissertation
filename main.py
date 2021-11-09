# Clock In Managment System Using Face Recognition

from tkinter import * 
import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p \n %x')
    label.config(text=string)
    label.after(1000, time)

# User Interface (Menu) 

window = tk.Tk()
window.geometry("1028x520")
window.resizable(True,False)
window.title("Clocking System")   

label=Label(window, font=("times new roman", 30, "bold"),bg="grey", fg="white")
label.pack(side=TOP, fill=X)
time()  

window.mainloop()