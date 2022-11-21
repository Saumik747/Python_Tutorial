"""
Practical 3:
Write a python program to add ‘ing’
at the end of a string (length at least 3).
If the given string already ends with ‘ing’
then add ‘ly’ instead. If the string length
of the given string is less than 3, leave it unchanged.
"""
ch='y'
ing='ing'
ly='ly'
while ch.lower()=='y':
    str2=input("Enter a String: ")
    if len(str2)>=3:
        if (str2.endswith('ing')):
            print("Result: ",str2.replace('ing',ly))
        else:
            print("Result: ",str2+ing)
        ch1=input("continue(y/n)?")
    


    else:
        print("Result: ",str2)
        ch1=input("continue(y/n)?")
