import sqlite3
conn=sqlite3.connect('saumik.db')
print("open database successfully")
n=int(input("Enter how many records you want to insert"))
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
conn.close()
