from pymongo import MongoClient
import gridfs
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Database script 

# Connection to the database
def mongo_conn():
    # if there is connection to db then
    try:
        conn = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # print the message or
        print("MongoDB connected", conn)
        return conn.Registration
        # if there is no connection then 
    except Exception as e:
        # print error message
        print("Error in mongo connection", e)

# Function to store/retrieve students to/from the database.
def store_retrieve(ID):
    # Stores the image on the database
    db = mongo_conn()
    # location of the file
    file_location = "images/" + ID.get() + ".jpg"
    # open the file 
    file_data = open(file_location, "rb")
    # read the file
    data = file_data.read()
    # store it in the database
    fs = gridfs.GridFS(db)
    fs.put(data, filename = ID.get())

    db = mongo_conn()
    # Retrieving the image from the database
    data = db.fs.files.find_one({'filename': ID.get()})
    # _id assigns a auto generated id in mongoDB 
    my_id = data['_id'] 
    fs = gridfs.GridFS(db)
    outputdata = fs.get(my_id).read()
    # saves the retrieved image in the downloads folder
    download_location = "download/" + ID.get() + ".jpg"
    output = open(download_location, "wb")
    output.write(outputdata)
    output.close()
    print("download completed")

# Function to save student logs to the database
def store_logs(ID, timeString, dateString):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["logs"]

    # saves student ID, time and date they have checked in.
    post = {"Student ID": ID, "Time": timeString, "Date": dateString}
    collection.insert_one(post)

# Function to save health check form details
def store_form(mobile_var, college_attend, confirmation):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]

    # saves students mobile number, college attending and the confirmation.
    post = {"Mobile Number": mobile_var.get(), "College": college_attend.get(), "Confirmation": confirmation.get()}
    collection.insert_one(post)

def store_email(ID):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["student_details"]

    post = {"Email": ID.get() + "@gmit.ie"}
    collection.insert_one(post)

def delete_student(deleteID):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["fs.files"]    

    # Delete student by ID.
    deleteStudentID = {"filename": deleteID.get()}
    collection.delete_one(deleteStudentID)
    print("[INFO] Student with ID: " + deleteID.get() + " has been deleted from the database.")

def delete_email(deleteID):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["student_details"]    

    # Delete student email.
    deleteEmail = {"Email": deleteID.get() + "@gmit.ie"}
    collection.delete_one(deleteEmail)

def delete_all():
    # Delete all registered students from the database.
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["student_details"]    
    collection2 = db["fs.files"] 
    collection3 = db["fs.chunks"] 

    # Delete each collection.
    collection.delete_many({})
    collection2.delete_many({})
    collection3.delete_many({})

    # Delete students completed form and logs.
    db2 = cluster["Students"]
    collection4 = db2["health_check_form"] 
    collection5 = db2["logs"] 

    # Delete each collection.
    collection4.delete_many({})
    collection5.delete_many({})
    print("[INFO] All data has been deleted from the database.")

def all_students(n):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["fs.files"]

    student_list = [['Students']]

    student_list.clear()
    student_list.append(["Students"])
    cursor = collection.find({})
    for text_fromDB in cursor:
        filename = str(text_fromDB['filename'].encode('utf-8').decode("utf-8"))
        student_list.append([filename])
    return student_list

def student_logs(n):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["logs"]

    logs_list = [['Student ID', 'Time', 'Date']]

    logs_list.clear()
    logs_list.append(["Student ID", "Time", "Date"])
    cursor = collection.find({})
    for text_fromDB in cursor:
        id = str(text_fromDB['Student ID'].encode('utf-8').decode("utf-8"))
        time = str(text_fromDB['Time'].encode('utf-8').decode("utf-8"))
        date = str(text_fromDB['Date'].encode('utf-8').decode("utf-8"))
        logs_list.append([id, time, date])
    return logs_list

def student_details(n):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["student_details"]

    details_list = [['Students Email']]

    details_list.clear()
    details_list.append(["Students Email"])
    cursor = collection.find({})
    for text_fromDB in cursor:
        email = str(text_fromDB['Email'].encode('utf-8').decode("utf-8"))
        details_list.append([email])
    return details_list

def health_check(n):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]

    form_list = [['Student Mobile Number', 'College Attending', 'Confirmation']]

    form_list.clear()
    form_list.append(["Student Mobile Number", "College Attending", "Confirmation"])
    cursor = collection.find({})
    for text_fromDB in cursor:
        mobile = str(text_fromDB['Mobile Number'].encode('utf-8').decode("utf-8"))
        college = str(text_fromDB['College'].encode('utf-8').decode("utf-8"))
        conf = str(text_fromDB['Confirmation'].encode('utf-8').decode("utf-8"))
        form_list.append([mobile, college, conf])
    return form_list

def total_students():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Registration"]
    collection = db["fs.files"]

    # number of documents in the collection
    totalStudents = collection.count_documents({})
    return totalStudents

def total_checkin():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["logs"]

    # number of documents in the collection
    totalCheckIns = collection.count_documents({})
    return totalCheckIns

def total_health_check():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]
 
    # number of documents in the collection
    totalForms = collection.count_documents({})
    return totalForms

def total_with_no_symptoms():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]

    # number of documents in the collection
    totalNoSymptoms = collection.count_documents({'Confirmation': "Yes"})
    return totalNoSymptoms

def total_with_symptoms():
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]

    # number of documents in the collection
    totalWithSymptoms = collection.count_documents({'Confirmation': "No"})
    return totalWithSymptoms