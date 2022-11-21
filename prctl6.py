"""
Practical 6:
Write a python program to convert a list of multiple integer
into single string.
"""
ch='y'
while ch.lower()=='y':
    lst=[]
    lst1=[]
    n=int(input("Enter Number of elements: "))
    str1=''
    for i in range(0,n):
        int1=int(input("Element: "))
        lst.append(int1)
        str1=str1+str(int1)
        
    print(lst)
    print(str1)
    ch=input("continue(y/n)? ")
