import sqlite3 as lite
import sys
try:
    con=lite.connect('test.db')
    cursor=con.cursor()
    id=int(input("Enter id:"))
    name=input("Enter the name:")
    cursor.execute("update company1 set name='"+name+"' where id = '"+str(id)+"' ")
    con.commit()
finally:
    con.close()
