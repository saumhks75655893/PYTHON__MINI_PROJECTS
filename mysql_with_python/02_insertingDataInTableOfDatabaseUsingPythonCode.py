# INSERTING VALUES OF THE TABLE BY USING PYTHON PROGRAMMS 

import mysql.connector as c
con = c.connect(host="localhost",user="root",passwd="75655893",database="STUDENT")

cursor = con.cursor()
Enroll = int(input("Enter the enrollment number : "))
Name = input("Enter the name of the student : ")
Address = input("Enter the address of the student : ")
Email = input("Enter the email address of the student : ")
Mobile = int(input("Enter the mobile number of the student : "))
FatherName = input("Enter the father name of the student : ")
MotherName = input("Enter the mother name of the student : ")
Semester = int(input("Enter the semester of the student : "))

query = "insert into studentDetails values({},'{}','{}','{}',{},'{}','{}',{})".format(Enroll,Name,Address,Email,Mobile,FatherName,MotherName,Semester)

cursor.execute(query)
con.commit()
print("Record inserted successfully.... ")




