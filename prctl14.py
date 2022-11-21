"""
Practical 14:
Write a python program that finds the largest file in the given directory.
"""
import os
ch='y'
while ch.lower()=='y':
    directory=input("Enter Directory: ")
    lis=os.listdir(directory)
    fname={}
    fsize=0
    for i in lis:
        fname[os.stat(i).st_size]=i
    for j in fname:
        if(int(j)>fsize):
            fsize=j
    print("Largest File is: ",fname[fsize])
    ch=input("Continue (y/n)?")
