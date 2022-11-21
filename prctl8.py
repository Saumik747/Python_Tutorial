""" Practical 8:
Write a python program to Perform Matrix Multiplication.
"""
ch='y'
while ch.lower()=='y':
    print("Enter value of rows and cols for both matrix")
    a=input("enter no of rows for a: ")
    b=input("enter no of columns for a: ")
    c=input("enter no of rows for b: ")
    d=input("enter no of columns for b: ")
    s=[]
    t=[]
    if(a==d):
        print("Matrix a")
        for e in range(0,int(a)):
            x=[]
            for f in range(0,int(b)):
                x.append(int(input("element ")))
            s.append(x)

        print("Matrix b")
        for e in range(0,int(c)):
            y=[]
            for f in range(0,int(d)):
                y.append(int(input("element ")))
            t.append(y)

 
       
    
        print("matrix a")
        for i in range(0,int(a)):
            for j in range(0,int(b)):
                print(s[i][j], end = " ")
            print()

        print("matrix b")
        for i in range(0,int(c)):
            for j in range(0,int(d)):
                print(t[i][j], end = " ")
            print()

        print("result matrix c")
        u=[[0 for i in range(int(d))] for i in range(int(a))]
    
        for i in range(0,len(s)):
            for j in range(0,len(t[0])):
                for k in range(0,len(t)):
                    u[i][j]+=s[i][k] * t[k][j]
                    

        for i in range(0,int(a)):
            for j in range(0,int(d)):
                print(u[i][j], end = " ")
            print()

    else:
        print("Matrix multiplication cannot be performed ,no of rows!= no of columns")
    ch=input("continue(y/n)? ")
