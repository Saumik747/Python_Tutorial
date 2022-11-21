ch='y'
class colors:
    def displaycolor(self,str1):
        rainbow={'v':'voilet',
             'i':'indigo',
             'b':'blue',
             'g':'green',
             'y':'yellow',
             'o':'orange',
             'r':'red'}
        if(str1.lower() in rainbow.keys()):
            print(rainbow[str1.lower()])
        else:
            raise KeyError("Color not found")


while ch.lower()=='y':
    str1=input("Enter Character: ")
    color1=colors()
    if((len(str1)==1 ) and(str1.isalpha()==True)) :
        
        color1.displaycolor(str1) 
        ch=input("Continue(y/n)? ")
    else:
        raise Exception("only Alphabets are allowed")
    
