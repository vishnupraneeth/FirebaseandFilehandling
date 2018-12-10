
import sqlite3 as sql
connection=sql.connect('important.db')
curs=connection.cursor()
curs.execute("Select * from Employee")
result=curs.fetchmany(7)
print(result)
connection.commit()
connection.close()
