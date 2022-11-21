"""
Practical 12:
Write a python program to create a dictionary
with key as first character and 
value as words starting with that character.
The program takes a string and creates a
dictionary with key as first character and value as words
starting with that character.
"""
    ch='y'
    while ch.lower()=='y':
        s=input("Enter String: ")
        s_chr=s.split()
        d={}#dictionary blank
        for s_chrs in s_chr:
            
            if(s_chrs[0] not in d.keys()):
                d[s_chrs[0].lower()]=[]
                d[s_chrs[0].lower()].append(s_chrs)
            else:
                if(s_chrs[0] in d.keys()):
                    
                    d[s_chrs[0].lower()].append(s_chrs)
        dnew = dict( sorted(d.items(), key=lambda x: x[0].lower()) )
        
        print("dictoinary \n",dnew)
        ch=input("Continue (y/n)?")
