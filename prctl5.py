"""
Practical 5:
Write a python program to create list by concatenating
a given list which range goes from 1 to n.
"""
ch='y'
while ch.lower()=='y':
    lst=[]
    lst1=[]
    m=int(input("Enter Number of elements: "))
    n=int(input("Enter range: "))
    str1=''
    for i in range(0,m):
        str1=input("Element : ")
        lst.append(str1)
    for x in range(1,n+1):
        for y in range(0,m):
            lst1.append(lst[y]+str(x))
                
    print(lst1)
    ch=input("continue(y/n)? ")
