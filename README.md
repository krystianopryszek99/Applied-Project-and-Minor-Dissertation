<p align="center">
  <img src="https://user-images.githubusercontent.com/57759154/162638159-53282ce7-70bf-40bf-8409-5d285f1f696d.png" width="350" height="150"/>
 </p>

# Applied Project and Minor Dissertation

| Project Title | Check In System Using Face Recognition | 
| --------------- | --------------- | 
| Course | BSc (Hons) in Software Development |
| Module | Applied Project and Minor Dissertation| 
| Student(s) | Krystian Opryszek | 
| Project Supervisor | Daniel Cregg | 
| Module Supervisor | Dr. John Healy |

## Table Of Content

- [Overview](#Overview)
- [Project Outline](#Project-Outline)
- [Project Features](#Project-Features)
- [How to run](#How-to-run)
- [Technologies used ](#Technologies-used)
- [Screencast](#Screencast)
- [References](#References)

## Overview

This repository contains my final project which is a Check In System using Face Recognition. The main idea of this project is to recognize students by their faces and check them in. In today's environment, people are forgetting their passwords/emails. The purpose of this project is so that no item is required to be carried or no password to be remembered, all it requires is the students’s face. Biometric authentication is very popular and I wanted to come up with a program that is user-friendly and authenticates users in a fast and smart way.

My goal is to have a fully working program that recognizes faces accurately and enables students to check in to college using mobile phones or kiosks. A kiosk is an idea that would be a standing station with kiosks at every door of GMIT. Due to the pandemic, students/lecturers have to fill out a health check form which not many people are aware of. The idea with kiosks would force students to fill them out on the way in.

The health check form is based on [GMIT Daily Health Check 2021](https://forms.office.com/Pages/ResponsePage.aspx?id=rs8Gj9UihEykbT2-PJNVjXOa1-is_qFErTzGrrpb_BBUMEVaUkpGME1CS0ZNRUQzOUVLVktMNTM5MCQlQCN0PWcu). A menu that displays the health check form is a short version of the official GMIT health check form. The form includes the following: *Mobile number, Selection of colleges that the student is attending, and if the student is confirming that he is symptom-free*.

## Project Outline

<p align="center">
  <img src="https://user-images.githubusercontent.com/57759154/162637538-f8b2865c-6980-4bc6-8363-bc684810fb21.PNG" />
</p>

**(1) Capture Image:** Using live stream with a camera, user’s face is captured based on their face encodings, such as the length between their eyebrows. 

**(2) Image Processing:** When the image is captured, it's being processed with the face encodings. 

**(3) Storing Data:** After the image is being captured and processed, the image gets stored on the database.

**(4) Matching:** The program is checking if the face checking-in matches any of the faces that are saved in the database.

**(5) Result:** When the match is true (successful), it will authenticate the user and successfully check him in.

## Project Features

This outlines the main features of the project. 

- Program is run using Python version 3.8.8 with some specified [here](#Technologies-used) libraries and tools. 
- Program recognizes faces by the face encodings.
- Program is capable of recognizing each student once saved in the database.
- Students logs are stored in the database.
- Health check form is required to be filled out before checking in.
- Students have to enter mobile number, email address, college attending and confirmation.
- Sends email after completing the health check form.
- Health check form details are stored in the database.
- Capable of checking-in by face.
- View and manage student's in admin's dashboard

## How to run 

1. Clone this repository onto your machine.
```
$ git clone https://github.com/krystianopryszek99/Applied-Project-and-Minor-Dissertation.git
```
2. Once you have cloned the repository, make sure your in the `Applied-Project-and-Minor-Dissertation/Application` directory.
3. Follow the [requirements](requirements.md) to ensure all software is installed before running the program.
4. To start the application, run the following command:
```
$ python main.py
```

## Technologies used 

- Python version 3.8.8 - Used to write code.
- MongoDB - Store images to the database.
- PyMongo - Tool for working with MongoDB.
- OpenCV - Real-time computer vision.
- Tkinter - Build GUI.
- Dlib - [See this for version](requirements.md).
- face_recognition - Recognizes faces.
- time - module provides time related functions.
- GridFS - Store and retrieve large files.
- email.message - Sends emails.

## Screencast
https://youtu.be/ZP84nHFpdl8

## References

- [Python](https://www.python.org/)
- [MongoDB](https://account.mongodb.com/account/login?signedOut=true)
- [PyMongo](https://docs.mongodb.com/drivers/pymongo/)
- [OpenCV](https://opencv.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Dlib](http://dlib.net/)
- [Face Recognition](https://pypi.org/project/face-recognition/)
- [time](https://docs.python.org/3/library/time.html)
- [GridFS](https://docs.mongodb.com/manual/core/gridfs/)
- [email.message](https://docs.python.org/3/library/email.message.html)
