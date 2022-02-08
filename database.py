from pymongo import MongoClient
import gridfs
from tkinter import * 
from tkinter import messagebox

# Stores and Retrieves users from the database 

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

# Function to store students to the database.
def store(name):
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
    print("upload completed")

# Function to retrieve students from the database.
def retrieve():
    db = mongo_conn()
    name = 'krystian.jpg'
    # Retrieving the image from the database
    data = db.fs.files.find_one({'filename': name})
    # _id assigns a auto generated id in mongoDB 
    my_id = data['_id'] 
    fs = gridfs.GridFS(db)
    outputdata = fs.get(my_id).read()
    # saves the retrieved image in the downloads folder
    download_location = "download/" + name
    output = open(download_location, "wb")
    output.write(outputdata)
    output.close()
    print("download completed")