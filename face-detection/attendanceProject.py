import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
#from tk import *


def clear():
    txt.delete(0, 'end')
    txt2.delete(0, 'end')


def TakeImage():
    cam = cv2.VideoCapture(0)
    count = 1
    while True:
        ret, img = cam.read()
        cv2.imshow("Taking Image", img)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # For Esc key
            print("Close")
            break
        elif k % 256 == 32:
            # For Space key
            Rno = (txt2.get())
            name = (txt.get())
            print("Image saved")
            file = 'C:/Users/dhruti/PycharmProjects/face-detection/face-detection/Images/'+name + " " + Rno + '.jpg'
            cv2.imwrite(file, img)
            count += 1
    cam.release()
    cv2.destroyAllWindows()


def profile():
    if(txt.get()=="" or txt2.get()==""):
            messagebox.showinfo('Result','Please provide complete details.')
    else:
            mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Attendance"
            )
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * from users")
            myresult=mycursor.fetchall()
            id=1
            for x in myresult:
                id+=1
            sql="insert into users(id,Name,Roll_no) values(%s,%s,%s)"
            val=(id,txt.get(),txt2.get())
            mycursor.execute(sql,val)
            mydb.commit()
            messagebox.showinfo('Result', 'Profile Saved')

def attendance():
    path = 'Images'
    images = []
    classNames = []
    myList = os.listdir(path)
    #print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)


    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    def markAttendance(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%d/%m/%y %H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('Webcam', img)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # For Esc key
            print("Close")
            break
    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo('Result', 'Attendance Taken')



#frontend--------------------------------------------------

window = tk.Tk()
window.title("Face Detection Based Attendance System")
window.geometry("1280x700")
window.resizable(True,True)
window.configure(background='#2d1345')

#main window------------------------------------------------
message3 = tk.Label(window, text="Face Detection Based Attendance System" ,fg="white",bg="#2d1345" ,width=60 ,height=1,font=('times', 29, ' bold '))
message3.place(x=10, y=10,relwidth=1)

#frames-------------------------------------------------
frame1 = tk.Frame(window, bg="white")
frame1.place(relx=0.11, rely=0.15, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="white")
frame2.place(relx=0.51, rely=0.15, relwidth=0.39, relheight=0.80)

#frame_headder
fr_head1 = tk.Label(frame1, text="New Registration", fg="white",bg="#edc75c" ,font=('times', 17, ' bold ') )
fr_head1.place(x=0,y=0,relwidth=1)

fr_head2 = tk.Label(frame2, text="Mark attendance", fg="white",bg="#edc75c" ,font=('times', 17, ' bold ') )
fr_head2.place(x=0,y=0,relwidth=1)

#registretion frame
lbl = tk.Label(frame1, text="Enter Name",width=20  ,height=1  ,fg="black"  ,bg="white" ,font=('times', 17, ' bold ') )
lbl.place(x=0, y=55)

txt = tk.Entry(frame1,width=32 ,fg="black",bg="#f0f4fa",highlightcolor="#00aeff",highlightthickness=3,font=('times', 15, ' bold '))
txt.place(x=55, y=88,relwidth=0.75)

lbl2 = tk.Label(frame1, text="Enter Roll No",width=20  ,fg="black"  ,bg="white" ,font=('times', 17, ' bold '))
lbl2.place(x=0, y=140)

txt2 = tk.Entry(frame1,width=32 ,fg="black",bg="#f0f4fa",highlightcolor="#00aeff",highlightthickness=3,font=('times', 15, ' bold ')  )
txt2.place(x=55, y=173,relwidth=0.75)

message0=tk.Label(frame1,text="Steps To Take Image",bg="white" ,fg="black"  ,width=39 ,height=1,font=('times', 16, ' bold '))
message0.place(x=7,y=275)

message1 = tk.Label(frame1, text="1)Press Space Key      2)Press Esc Key" ,bg="white" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('times', 15, ' bold '))
message1.place(x=7, y=300)

#BUTTONS----------------------------------------------
clearButton = tk.Button(frame1, text="Clear", command=clear, fg="black", bg="#8588ed", width=11, activebackground = "white", font=('times', 12, ' bold '))
clearButton.place(x=55, y=230,relwidth=0.29)

takeImg = tk.Button(frame1, text="Take Image", command=TakeImage, fg="black", bg="#8588ed", width=34, height=1, activebackground = "white", font=('times', 16, ' bold '))
takeImg.place(x=30, y=350,relwidth=0.89)

trainImg = tk.Button(frame1, text="Save",command=profile, fg="black", bg="#8588ed", width=34, height=1, activebackground = "white", font=('times', 16, ' bold '))
trainImg.place(x=30, y=430,relwidth=0.89)

trackImg = tk.Button(frame2, text="Take Attendance",command=attendance, fg="black", bg="#8588ed", height=1, activebackground = "white" ,font=('times', 16, ' bold '))
trackImg.place(x=30,y=60,relwidth=0.89)

img = ImageTk.PhotoImage(Image.open("C:/Users/dhruti/PycharmProjects/face-detection/face-detection/attendance_img.jpg"))
panel = tk.Label(frame2, image = img)
panel.place(x=30,y=120,relwidth=0.89)

#closing lines------------------------------------------------
window.mainloop()

