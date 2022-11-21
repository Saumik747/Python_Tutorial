
import sqlite3
conn=sqlite3.connect('demo.db')
print("open database successfully")
n=int(input("Enter how many records you want to insert"))


print("\n before insertion")
cursor=conn.execute("SELECT id,name,age,address,salary from company")
for row in cursor:
    print("ID:",row[0])
    print("NAME:",row[1])
    print("AGE:",row[2])
    print("ADDRESS",row[3])
    print("SALARY",row[4])

for i in range(0,n):
    a=int(input("ID: "))
    b=input("NAME: ")
    c=int(input("Age: "))
    d=input("Address: ")
    e=int(input("Salary; "))
    str1="Insert into COMPANY(id,name,age,address,salary)values('"+ str(a) +"','"+ b+ "','"+ str(c) +"','"+ d +"','"+ str(e)+"')"
    conn.execute(str1)
conn.commit()
print("Records inserted successfully")

print("\n after insertion")
cursor=conn.execute("SELECT id,name,age,address,salary from company")
for row in cursor:
    print("ID:",row[0])
    print("NAME:",row[1])
    print("AGE:",row[2])
    print("ADDRESS",row[3])
    print("SALARY",row[4])

conn.close()

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



rc=[]
n=int(input("Enter how many records you want to insert"))
for i in range(0,n):
    a=int(input("ID: "))
    b=input("NAME: ")
    c=int(input("Age: "))
    d=input("Address: ")
    e=int(input("Salary; "))
    val1=(a,b,c,d,e)
    rc.append(val1)

print("\n before insertion")
beforeins()
str1="Insert into emp(id,name,age,addr,salary) values(%s,%s,%s,%s,%s)"
#print(rc)
if len(rc)>1:
    mcursor.executemany(str1,rc)
else:
    mcursor.execute(str1,rc[0])
mydb.commit()
print(mcursor.rowcount,"Records inserted successfully")

print("\n after insertion")
beforeins()
mcursor.close()
"""
