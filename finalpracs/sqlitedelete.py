import sqlite3 as lite
import sys
try:
    con=lite.connect('test.db')
    cursor=con.cursor()
    id=int(input("Enter id:"))
    #name=input("Enter the name:")
    cursor.execute("delete from company1  where id = '"+str(id)+"' ")
    print("Record Delete successfully")
    con.commit()
finally:
    con.close()
