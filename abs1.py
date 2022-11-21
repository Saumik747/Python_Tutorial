from abc import ABC, abstractmethod
import math
ch='y'
class shape(ABC):
    @abstractmethod
    def area(self,a,b):
        pass
    
    @abstractmethod
    def perimeter(self,a,b):
        pass

class rectangle(shape):
    def area(self,a,b):
        r=a*b
        print("area of rectangle: ",r)

    def perimeter(self,a,b):
        s=a+b
        r=2*s
        print("perimeter:",r)
        

class triangle(shape):
    def area(self,a,b):
        s=a*b
        r=0.5*s
        print("area of triangle: ",r)

    def perimeter(self,a,b):
        c=int(input("Enter Length for third side of traingle"))
        s=a+b+c
        
        print("perimeter:",s)


class circle(shape):
    def area(self,a,b):
        s=a*b
        r=3.14*s*s
        print("area of circle: ",r)

    def perimeter(self,a,b):
        
        s=3.14*a*b
        r=2*s
        print("perimeter:",r)

class rhombus(shape):
    def area(self,a,b):
        s=a*b
        r=s/2
        print("area of rhombus: ",r)

    def perimeter(self,a,b):
        x=(a*a)+(b*b)
        r=2*math.sqrt(x)
        print("perimeter:",r)

    
while ch.lower()=='y':
    print("Select option to search from below \n")
    print("1. rectangle ")
    print("2. triangle")
    print("3. circle")
    print("4. rhombus")
    print("5. show all")
    d1=rectangle()
    d2=triangle()
    d3=circle()
    d4=rhombus()
    otp=int(input("Enter option"))
    if(otp==1):
        a=int(input("Enter length of rectangle: "))
        b=int(input("Enter breadth of rectangle: "))
        d1.area(a,b)
        d1.perimeter(a,b)

    elif(otp==2):
        a=int(input("Enter base of triangle: "))
        b=int(input("Enter height of traingle: "))
        d2.area(a,b)
        d2.perimeter(a,b)

    elif(otp==3):
        a=int(input("Enter radius of circle: "))
        d3.area(a,1)
        d3.perimeter(a,1)

    elif(otp==4):
        a=int(input("Enter d1 of rhombus: "))
        b=int(input("Enter d2 of rhombus: "))
        #c=int(input("Enter side of rhombus: "))
        d4.area(a,b)
        d4.perimeter(a,b)

    elif(otp==5):
        a1=int(input("Enter length of rectangle: "))
        a2=int(input("Enter breadth of rectangle: "))

        b1=int(input("Enter base of triangle: "))
        b2=int(input("Enter height of traingle: "))

        c1=int(input("Enter radius of circle: "))

        e1=int(input("Enter d1 of rhombus: "))
        e2=int(input("Enter d2 of rhombus: "))
        #e3=int(input("Enter side of rhombus: "))
        

        




        d1.area(a1,a2)
        d1.perimeter(a1,a2)

        d2.area(b1,b2)
        d2.perimeter(b1,b2)

        d3.area(c1,1)
        d3.perimeter(c1,1)


        d4.area(e1,e2)
        d4.perimeter(e1,e2)

        
        
        
        

    else:
        print("please select suitable option")
    ch=input("continue (y/n)?")
        
