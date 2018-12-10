import sqlite3 as sql
connection = sql.connect('vishnu.db')
curs=connection.cursor()
cur=curs.execute("select * from s")
for row in cur :
    print("Name : " , row[0])
connection.commit()
connection.close()
