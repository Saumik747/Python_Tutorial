"""
write a python program to accept 2 integers and 1 arithmetic operator
find following user defined exception
i.)Number of Arguments less than 3 raise:"illegal no. of args"
ii.)if operator is not arithmetic operator raise:"invalid operator"
iii.)if result is negative raise: "result exception"
"""

ch='y'
def funop(*args):
    a=args[0]
    b=args[1]
    op=args[2]
    d1=a+b
    d2=a-b
    d3=a*b
    d4=a/b
    d5=a%b
    #chkres(d1,d2,d3,d4,d5)
    if(len(args)==3):
        if(op=='+' and d1>0):
            print("a+b:",d1)
                
        elif(op=='-' and d2>0):
            print("a-b:",d2)

        elif(op=='*' and d3>0):
            print("a*b:",d3)

        elif(op=='/' and d4>0):
            print("a/b:",d4)

        elif(op=='%' and d5>0):
            print("a%b:",d5)
            
        else:
            chkres(d1,d2,d3,d4,d5)
    else:
       raise Exception("Illegal No of Args")

def chkres(d1,d2,d3,d4,d5):
    if(d1<0 or d2<0 or d3<0 or d4<0 or d5<0   ):
        raise Exception("Negative result Exception")
    else:
        pass

    
while ch.lower()=='y':
    x=int(input("Enter value for num1: "))
    y=int(input("Enter value for num2: "))
    op=input("Enter Operator: ")
    
    lst_op=['+','-','%','*','/']

    if(op in lst_op):
        funop(x,y,op)
    else:
        raise Exception("Invalid Operator")
        

    ch=input("Continue (y/n)?")
    #funop(x,y,op,"arg4")
    #ch=input("Continue (y/n)?")
        

    
    
