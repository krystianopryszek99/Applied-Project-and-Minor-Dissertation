<p align="center">
  <img src="https://user-images.githubusercontent.com/57759154/140659027-396b5850-35dd-408e-8a57-51adbcfd9bdc.png" />
 </p>

# Applied Project and Minor Dissertation

| Project Title | Clocking System Using Face Recognition | 
| --------------- | --------------- | 
| Course | BSc (Hons) in Software Development |
| Module | Applied Project and Minor Dissertation| 
| Student(s) | Krystian Opryszek | 
| Project Supervisor | Daniel Cregg | 
| Module Supervisor | Dr. John Healy |

## Table Of Content
- [Overview](#Overview)
- [Project Outline](#Project-Outline)
- [How to run](#How-to-run)
- [Demo](#Demo)
- [Technologies used ](#Technologies-used)
- [References](#References)

# Overview
This repository contains my final project which is a Clocking Management System using Face Recognition. The main idea of this project is to recognize users by their faces and check them in. In today's environment, people are forgetting their passwords/emails. The purpose of this project is so that no item is required to be carried or no password to be remembered, all it requires is the user’s face. Biometric authentication is very popular and I wanted to come up with a program that is user-friendly and authenticates users in a fast and smart way.

My goal is to have a fully working program that recognizes faces accurately and enables users to check in to college using mobile phones or kiosks. A kiosk is an idea that would be a standing station with kiosks at every door of GMIT. Due to the pandemic, students/lecturers have to fill out a health check form which not many people are aware of. The idea w kiosks would force students to fill them out on the way in.

The health check form is based on [GMIT Daily Health Check 2021](https://forms.office.com/Pages/ResponsePage.aspx?id=rs8Gj9UihEykbT2-PJNVjXOa1-is_qFErTzGrrpb_BBUMEVaUkpGME1CS0ZNRUQzOUVLVktMNTM5MCQlQCN0PWcu). A menu that displays the health check form is a short version of the official GMIT health check form. The form includes the following: *Mobile number, Selection of colleges that the student is attending, and if the student is confirming that he is symptom-free*.

# Project Outline

<p align="center">
  <img src="https://user-images.githubusercontent.com/57759154/149411479-d1b50316-87af-4a43-b857-93811b22b23a.png" />
</p>

**(1) Capture Image:** Using live stream with a camera, user’s face is captured based on their face encodings, such as the length between their eyebrows. 

**(2) Image Processing:** When the image is captured, it's being processed with the face encodings. 

**(3) Storing Data:** After the image is being captured and processed, the image gets stored on the database.

**(4) Matching:** The program is checking if the face checking-in matches any of the faces that are saved in the database.

**(5) Result:** When the match is true (successful), it will authenticate the user and successfully check him in.

# How to run 
1. Clone this repository onto your machine.
```
$ git clone https://github.com/krystianopryszek99/Applied-Project-and-Minor-Dissertation.git
```
2. Once you have cloned the repository, make sure your in the `Applied-Project-and-Minor-Dissertation` directory.
3. Follow the [requirements](requirements.md) to ensure all software is installed before running the program.
4. To start the application, run the following command:
```
$ python main.py
```

# Demo

This is a current version of the program running, design and functionality are to be changed or updated.   

![demo](https://user-images.githubusercontent.com/57759154/149583812-2d97607e-8048-4c9e-9e17-10ac95042dc8.gif)

# Technologies used 

- Python version 3.8.8 - Used to write code.
- MongoDB - Store images to the database.
- PyMongo - Tool for working with MongoDB.
- OpenCV - Real-time computer vision.
- Tkinter - Build GUI.
- Dlib - [See this for version](requirements.md)
- face_recognition - Recognizes faces
- GridFS - Store and retrieve large files.

# References

- [Python](https://www.python.org/)
- [MongoDB](https://account.mongodb.com/account/login?signedOut=true)
- [PyMongo](https://docs.mongodb.com/drivers/pymongo/)
- [OpenCV](https://opencv.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Dlib](http://dlib.net/)
- [Face Recognition](https://pypi.org/project/face-recognition/)
- [GridFS](https://docs.mongodb.com/manual/core/gridfs/)

