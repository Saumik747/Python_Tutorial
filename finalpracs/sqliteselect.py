import sqlite3
conn=sqlite3.connect('test.db')
print("open database successfully")
cursor=conn.execute("SELECT id,name,age,address,salary from company1")
for row in cursor:
    print("ID:",row[0])
    print("NAME:",row[1])
    print("AGE:",row[2])
    print("ADDRESS",row[3])
    print("SALARY",row[4])
print("Operation done successfully")
conn.close()
