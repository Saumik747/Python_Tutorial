"""
Practical 4:
Write a Python Program to get a string where all
occurrences of its first character have been changed
to ‘@/#/$’ except the first char itself.
"""
ch='y'
while ch.lower()=='y':
    str2=input("Enter a String :")
    str3=input("Enter a character to replace: ")
    if len(str2)>=3:
        str4=str2[0]+str2[1:].replace(str2[0],str3)
        print("Result: ",str4)
    else:
        print("Empty String")
    ch=input("continue(y/n)?")
