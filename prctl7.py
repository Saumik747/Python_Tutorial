""" Practical 7:
Write a python program to transpose a matrix.
"""
ch='y'
while ch.lower()=='y':
    a=input("enter no of rows ")
    b=input("enter no of columns ")
    y=[]
    z=[]
    for e in range(0,int(a)):
        x=[]
        for f in range(0,int(b)):
            x.append(int(input("element ")))
        y.append(x)

    for i in range(0,int(a)):
        for j in range(0,int(b)):
            print(y[i][j], end = " ")
        print()
    print("transposing matrix")
    for i in range(0,int(b)):
        for j in range(0,int(a)):
            print(y[j][i], end = " ")
        print()
       
    ch=input("continue(y/n)? ")
