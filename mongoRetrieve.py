from pymongo import MongoClient
import gridfs

# Retrieves users from the database 

# Connection to the database
def mongo_conn():
    # if there is connection to db then
    try:
        conn = MongoClient("mongodb+srv://krystianopryszek:<password>@cluster0.sikdk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # print the message or
        print("MongoDB connected", conn)
        return conn.Images
        # if there is no connection then 
    except Exception as e:
        # print error message
        print("Error in mongo connection", e)

def retrieve():
    db = mongo_conn()
    name = 'elon.jpg'
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