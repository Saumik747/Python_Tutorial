"""
import sqlite3
import sys
def beforeupd():
    conn=sqlite3.connect('demo.db')
    print("open database successfully")
    cursor=conn.execute("SELECT id,name,age,address,salary from company")
    for row in cursor:
        print("ID:",row[0])
        print("NAME:",row[1])
        print("AGE:",row[2])
        print("ADDRESS",row[3])
        print("SALARY",row[4])
        print("Operation done successfully")

try:
    con=sqlite3.connect('demo.db')
    
    cursor=con.cursor()
    
    id=int(input("Enter id:"))
    name=input("Enter the name:")
    print("\n before update")
    beforeupd()
    cursor.execute("update company set name='"+name+"' where id = '"+str(id)+"' ")
    con.commit()
    print("\n after update")
    beforeupd()
finally:
    con.close()
"""

import mysql.connector as mysql
import mysql.connector as mysql
cred=["localhost","root","","demo"]
mydb=mysql.connect(host="localhost",user=cred[1],password="",database=cred[3])
mcursor=mydb.cursor()

def beforeins():
    cred=["localhost","root","","demo"]
    mydb=mysql.connect(host=cred[0],user=cred[1],password="",database=cred[3])
    mcursor=mydb.cursor()
    mcursor.execute("SELECT id,name,age,addr,salary from emp")
    mcur=mcursor.fetchall()
    for row in mcur:
        print("ID:",row[0])
        print("NAME:",row[1])
        print("AGE:",row[2])
        print("ADDRESS",row[3])
        print("SALARY",row[4])

s_id=int(input("Enter id:"))
name=input("Enter the name:")

print("\n before updation")
beforeins()
strupd="update emp set name = %s where id =%s"
val=(name,s_id)
mcursor.execute(strupd,val)
mydb.commit()
print("\n after updation")
beforeins()
mydb.close()


