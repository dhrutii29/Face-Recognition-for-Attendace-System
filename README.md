# Face-Recognition-for-Attendance-System
ML based project

## Introduction
Face recognition algorithms can extract features from a face image namely positions of forehead, eyes, nose, mouth, chin, jaws. 
Face Landmarks – There are 68 specific points (called landmarks) that exist on every face. 
Face Encodings – This is the 128 encoding feature vector from a pretrained network over millions of images. 


## Technology used
Python 3\
SQL


## Libraries
opencv-python\
numpy\
face_recognition\
datetime\
tkinter\
pillow\
mysql-connector-python\
cmake\
dlib\
os


## Description
Firstly, run the Database.py file which will create a database "Attendance" and a table "users" in the MySql server. 
Next run the main file that is AttendanceProject.py
On running this particular file a python application window will open up. Enter your name and roll no and click the save button to add your profile to the SQL server. Next click on the Take image button which will capture your image and then store it under the images folder. The instructions for capturing image are listed there itself. Once an individual has saved his/her profile he just needs to click the Take Attendance button and the webcam will come up. Recognition will be done and attendance will be stored into the attendance.csv file with the current date and time.


## Conclusion
Face recognition library being a high level deep learning library helps in identifying faces accurately. 
We’ve then used this to build a face attendance system which can be helpful in offices, 
schools or any other place reducing manual labour and automatically updating the attendance records in day-to-day life. 
This also notes down the time of arrival thus can acquire information about people coming in late after a specified time.
Thus it saves time and effort, especially if it is a lecture with a huge number of students. 



![project](https://user-images.githubusercontent.com/74110370/109301033-551a2300-785d-11eb-9816-9286211f6265.PNG)
