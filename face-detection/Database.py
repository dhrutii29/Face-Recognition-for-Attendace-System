import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", passwd="")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE Attendance")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

mydb=mysql.connector.connect(
host="localhost",
    user="root",
    passwd="",
    database="Attendance"
)
mycursor=mydb.cursor()
mycursor.execute("create table users(id int primary key,Name varchar(50),Roll_no int)")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
