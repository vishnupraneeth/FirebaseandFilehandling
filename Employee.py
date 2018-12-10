

import sqlite3 as sql
connection=sql.connect('important.db')
while True :
    
    Empid=int(input("Enter Employee id : "))
    Name=input("Enter Company Name : ")
    Age=int((input("Enter Age of the person : ")))
    Salary=float((input("Enter Salary of the person : ")))
    curs = connection.cursor()
#curs.execute("create table Employee(Empid,Name ,Age,Salary)")
    curs.execute("insert into Employee values(?,?,?,?)",(Empid,"Name",Age,Salary))
    ip=input("Press Y/y to continue")

    if ip=="Y" or ip=="y":
        continue
    else:
        break
    

connection.commit()
connection.close()
