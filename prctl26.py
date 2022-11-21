"""
import sqlite3
conn=sqlite3.connect('demo.db')
conn.execute('''CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL);''')
print("Table created")
conn.close()
"""
import mysql.connector as mysql
cred=["localhost","root","","demo"]
mydb=mysql.connect(host=cred[0],user=cred[1],password="",database=cred[3])
mcursor=mydb.cursor()
mcursor.execute('''CREATE TABLE emp1
(id INT PRIMARY KEY NOT NULL,
 name TEXT NOT NULL,
 age INT NOT NULL,
 addr CHAR(50),
 salary REAL);''')
print('table created successfully')
mydb.close()
