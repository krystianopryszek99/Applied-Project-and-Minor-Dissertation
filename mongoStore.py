from pymongo import MongoClient
import gridfs

# Stores users from the database 

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