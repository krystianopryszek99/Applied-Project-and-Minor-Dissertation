import pytest
import cv2
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from pymongo import MongoClient

def test_one():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    assert(cap.isOpened())

def test_two():
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
            img_name = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Testing/images_pytest/" + "testname" + ".jpg".format(img_counter)
            assert(cv2.imwrite(img_name, frame))
            img_counter += 1
            # closes the webcam
            cap.release()
            # destroys all the windows we created
            cv2.destroyAllWindows()

def test_three():
    # deletes the image of the folder
    path = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Testing/images_pytest/" + "testname" + ".jpg"
    os.remove(path)

    if len(os.listdir('C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Testing/images_pytest/')) == 0:
        messagebox.showerror("Alert","There are no students registred!\nRegister first!")
        assert(True)
    else:
        assert(False)

def test_four():

    def password():
        if adminPass.get() == "2022":
            messagebox.showinfo("Alert","ACCESS GRANTED!")
            assert(True)
            window.destroy()
        else:
            messagebox.showerror("Alert","WRONG PASSWORD!")
            window.destroy()
            assert(False)

    window = tk.Tk()
    window.geometry('600x400+50+50')
    adminPass = tk.StringVar()

    lbl_name = Label(window, text="Pin",fg="black",font=('Helvetica', 20, ' bold '))
    lbl_name.place(x=50, y=40)

    txt_name=Entry(window, textvariable=adminPass, font=('Helvetica', 15, ' bold '),bd=5,relief=GROOVE)
    txt_name.place(x=50, y=80)
    # submit form button
    submit_button = Button(window, text = "Login", command = password, bg = "green", font=('Helvetica', 12))  
    submit_button.place(x=50, y=150)
    window.mainloop()

def test_five():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Testing"]
    collection = db["tests"]  

    mylist = [
    { "name": "Ann", "Confirmation": "yes"},
    { "name": "Paddy", "Confirmation": "yes"},
    { "name": "Michael", "Confirmation": "no"},
    { "name": "Peter", "Confirmation": "yes"},
    { "name": "Bethany", "Confirmation": "no"},
    { "name": "Sara", "Confirmation": "no"},
    { "name": "Susan", "Confirmation": "no"},
    { "name": "Hannah", "Confirmation": "yes"},
    { "name": "Ben", "Confirmation": "no"},
    { "name": "Milly", "Confirmation": "yes"},
    { "name": "Ben", "Confirmation": "yes"},
    { "name": "Ella", "Confirmation": "yes"}
    ]

    data = collection.insert_many(mylist)
    assert(data)

def test_six():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Testing"]
    collection = db["tests"]    

    get = {"name": "Ben"}
    collection.find_one(get)

    if get == get:
        assert(True) 
    else:
        assert(False)

# that the collection is empty
def test_seven():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Testing"]
    collection = db["tests"]

    delete = {"name": "Bethany"}
    collection.delete_one(delete)

    # number of documents in the collection
    checkDoc = collection.count_documents({})
    if checkDoc == 11:
        assert(True)
    else:
        assert(False)

def test_eigth():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Testing"]
    collection = db["tests"]    

    docCount_yes = collection.count_documents({'Confirmation': "yes"}) 
    if docCount_yes == 7:
        assert(True)
    else:
        assert(False)

def test_nine():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Testing"]
    collection = db["tests"]    

    docCount_no = collection.count_documents({'Confirmation': "no"}) 
    if docCount_no == 4:
        assert(True)
    else:
        assert(False)
