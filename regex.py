import re
ch='y'
while ch.lower()=='y':
    str1=input("Enter Your String: ")
    p1 = '[A-Z]'
    p2='[a-z]'
    p3 = '[0-9]'
    p4='[$#@]'
    n=len(str1)
    if(n>=6 and n<=16 ):
        if((re.search(p1,str1)) and (re.search(p2,str1)) and (re.search(p3,str1)) and (re.search(p4,str1))):  
                                                            print("Valid Password")
        else:
            print("Passsword must contain 1 uppercase,1 lowecase alphabets,1 numeric and 1 special character")

    else:
        print("Password length min=6 and max = 16 characters")
    ch=input("continue (y/n)?")
        

