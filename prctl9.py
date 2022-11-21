""" Practical 9:
A string with paranthesis is well bracketed if all
paranthesis are matched i.e every opening bracket has a
matching closing bracket and vice versa.
Write a python program having function wellbrackered(s)
that takes string s containing parenthesis and return True
if s is well bracketed else False 

Hint: Keep track of nesting depth of brackets.Intially the depth is 0,The depth increases with each opening bracket and decreases with each closing bracket.What are the constraints on the value of nesting depth to be wellbracket?
Ex:wellbracketed(“22”))
False
Wellbracketed”(a+b)(a-b)”
True
"""
def wellbracketed(exprs):
    a1=exprs.count("(")
    a2=exprs.count(")")
    if(a1==a2):
      return True
    else:
      return False
ch='y'
while ch.lower()=='y':
    exprs=input("Enter Expression: ")
    print(wellbracketed(exprs))
    ch=input("continue(y/n)?")
    
