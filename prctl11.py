ch='y'
def ascending(lst1):
    val=""
    for i in range(0,len(lst)-1):
        if(lst[i]>lst[i+1]):
            return False
    return True
           
    
    
    
        
while ch.lower()=='y':
    lst=[]
    n=input("Enter size of list: ")
    for i in range(0,int(n)):
        a=int(input("Element: "))
        lst.append(a)
    print("list: ",lst)
    print(ascending(lst))
   

   
    ch=input("Continue (y/n)?")
