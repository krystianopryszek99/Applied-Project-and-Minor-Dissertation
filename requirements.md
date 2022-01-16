# Installation Process

*Note: You can skip step 1 if you already have Python installed on your machine.*

## Step-by-step 

1. First make sure you have python 3.8.8 installed. You may consider using latest version of python but you will be required to install different version of dlib. You can dowload python from here: [take me there](https://www.python.org/downloads/). 

    *Note: Make sure to tick `pip` when instaling Python, it will be needed later in the installation*

<p align="center">
  <img src="https://user-images.githubusercontent.com/57759154/149581288-b6e48d2c-6c33-4a4b-a280-626bc169fa24.png" />
</p>

3. Install Dlib from here: [take me there](https://github.com/pratyusa98/face-recognition_dlib_library). Make sure it's the version specified below:
```
dlib-19.19.0-cp38-cp38-win_amd64.whl
```
  - When you have Dlib installed, open your cmd and enter: 
  
  ```
  pip install "path"
  ``` 
  *Note: path is where you have dlib installed with `.whl` at end.*
  
3. Install OpenCV:
```
pip install opencv-python
```
4. Install Face recognition:
```
pip install face_recognition
```
5. Install PyMongo
```
pip install pymongo
```

*Now you should be able to run the program. Follow the instructions on how to run the program here:* [Take me there](README.md)