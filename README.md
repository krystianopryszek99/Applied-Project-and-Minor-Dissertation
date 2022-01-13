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
- [Technologies used ](#Technologies-used)
- [Refrences](#Refrences)


# Overview
This repository contains my final project which is a Clocking Management System using Face Recognition. The main idea of this project is to recognize users by their faces and check them in. In today's environment, people are forgetting their passwords/emails. The purpose of this project is so that no item is required to be carried or no password to be remembered, all it requires is the user’s face. Biometric authentication is very popular and I wanted to come up with a program that is user-friendly and authenticates users in a fast and smart way.

My goal is to have a fully working program that recognizes faces accurately and enables users to check in to college using mobile phones or kiosks. A kiosk is an idea that would be a standing station with kiosks at every door of GMIT. Due to the pandemic, students/lecturers have to fill out a health check form which not many people are aware of. The idea w kiosks would force students to fill them out on the way in.

# Project Outline

**Capture Image:** Using live stream with a camera, user’s face is captured based on their face encodings, such as the length between their eyebrows. 

**Image Processing:** When the image is captured, it's being processed with the face encodings. 

**Storing Data:** After the image is being captured and processed, the image gets stored on the database.

**Matching:** The program is checking if the face checking-in matches any of the faces that are saved in the database.

**Result:** When the match is true (successful), it will authenticate the user and successfully check him in.

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

# Technologies used 
- Python version 3.8.8
- MongoDB
- openCV

# References


