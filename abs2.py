from abc import ABC, abstractmethod
ch='y'
class myclass(ABC):
    @abstractmethod
    def si(self,p,r,n):
        pass
    
    @abstractmethod
    def ci(self,p,r,n):
        pass

class simple(myclass):
    def si(self,p,r,n):
        rsi=(p*r*n)/100
        print("Simple Interest ",rsi)

    def ci(self,p,r,n):
        pass

class compound(myclass):
    def si(self,p,r,n):
        pass

    def ci(self,p,r,n):
        c=p * (pow((1 + r / 100), n))
        print("Compound Interest ",c)
        

    
while ch.lower()=='y':
    p=int(input("Enter principle ammount"))
    r1=9.25
    r2=8.5
    #=int(input("Enter rate of interest"))
    n=int(input("Enter Time in years"))
    print("Select option to search from below \n")
    print("1. simple Interest \n 2. compound Interest \n 3. show both")
    
    d1=simple()
    d2=compound()
    
    otp=int(input("Enter option: "))
    if(otp==1):
        d1.si(p,r1,n)
        #d1.ci(p,r2,n)

    elif(otp==2):
        #d2.si(p,r1,n)
        d2.ci(p,r2,n)

    elif(otp==3):
        d1.si(p,r1,n)
        #d1.ci(p,r2,n)

        #d2.si(p,r,n)
        d2.ci(p,r2,n)
        
        
        

    else:
        print("please select suitable option")
    ch=input("continue (y/n)?")
        
