"""
Practical 15:
Write a python program to display files under specific directory.
"""
import os
ch='y'
while ch.lower()=='y':
    directory=input("Enter the Directory: ")
    #print(os.listdir(directory),end=" ")
    for i in os.listdir(directory):
        print(i)
    ch=input("check for another directory (y/n)?")
#for i in os.listdir(directory):
#    print(i)
