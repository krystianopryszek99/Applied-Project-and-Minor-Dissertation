from pymongo import MongoClient
import gridfs
from tkinter import * 
from tkinter import messagebox

# Database script 

# Connection to the database
def mongo_conn():
    # if there is connection to db then
    try:
        conn = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # print the message or
        print("MongoDB connected", conn)
        return conn.Images
        # if there is no connection then 
    except Exception as e:
        # print error message
        print("Error in mongo connection", e)

# Function to store/retrieve students to/from the database.
def store_retrieve(name):
    # Stores the image on the database
    db = mongo_conn()
    # location of the file
    file_location = "images/" + name.get() + ".jpg"
    # open the file 
    file_data = open(file_location, "rb")
    # read the file
    data = file_data.read()
    # store it in the database
    fs = gridfs.GridFS(db)
    fs.put(data, filename = name.get())
    messagebox.showinfo("Info", "Upload Completed!")

    db = mongo_conn()
    # Retrieving the image from the database
    data = db.fs.files.find_one({'filename': name.get()})
    # _id assigns a auto generated id in mongoDB 
    my_id = data['_id'] 
    fs = gridfs.GridFS(db)
    outputdata = fs.get(my_id).read()
    # saves the retrieved image in the downloads folder
    download_location = "download/" + name.get() + ".jpg"
    output = open(download_location, "wb")
    output.write(outputdata)
    output.close()
    print("download completed")

# Function to save student logs to the database
def store_logs(name, timeString, dateString):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["logs"]

    # saves student name, time and date they have checked in.
    post = {"Name": name, "Time": timeString, "Date": dateString}
    collection.insert_one(post)

# Function to save health check form details
def store_form(mobile_var,email_var, college_attend, confirmation):
    cluster = MongoClient("mongodb+srv://new-user_31:lCwmwIWHsuN4vJwQ@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Students"]
    collection = db["health_check_form"]

    # saves students mobile number, college attending and the confirmation.
    post = {"Mobile Number": mobile_var.get(), "Email": email_var.get(), "College": college_attend.get(), "Confirmation": confirmation.get()}
    collection.insert_one(post)