""" Practical 2:
Write a python Program to get a string made of the first 2 and last 2 character from a given string. If the string length is less than 2, return “Empty” instead of empty string
"""

def prbstmt2():
    ch='y'
    while ch.lower()=='y':
      str1=input("Enter a String: ")
      if len(str1)>=2:
          print("Expected Result: ",str1[0:2]+str1[-2:])
      else:
          print("Empty String(String len<2)")
      ch=input("want to continue(y/n)")
prbstmt2()
