"""Practical1 Write a python program to count number of character in a string """
ch='y'
while ch.lower()=='y':
    str1 = input ("Enter the string: ")
    d = dict()
    for c in str1:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    print(d)
    ch=input("Continue(y/n)? ")
