"""
import sqlite3
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
conn.close()
"""
import mysql.connector as mysql
cred=["localhost","root","","demo"]
mydb=mysql.connect(host=cred[0],user=cred[1],password="",database=cred[3])
mcursor=mydb.cursor()
mcursor.execute("SELECT id,name,age,addr,salary from emp")
mcur=mcursor.fetchall()
print("records\n")
for row in mcur:
    print("ID:",row[0])
    print("NAME:",row[1])
    print("AGE:",row[2])
    print("ADDRESS",row[3])
    print("SALARY",row[4])
mcursor.close()
