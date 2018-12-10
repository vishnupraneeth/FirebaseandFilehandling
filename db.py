import sqlite3 as sql
connection = sql.connect('vishnu.db')
curs=connection.cursor()
curs.execute("create table s(name,age)")
curs.execute("insert into s values('Ravi',23)")

connection.commit()
connection.close()
