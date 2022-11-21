""" List rotation """
ch='y'
def rotatelist(lst,k):
    lstn=[]
    if k>0:
        lstn = lst[-k:] + lst[:-k]
        return lstn
    else:
        return lst

while ch.lower()=='y':
    lst=[]
    n=input("Enter size of list: ")
    k=input("Enter No of rotations: ")
    for i in range(0,int(n)):
        a=input("Element: ")
        lst.append(int(a))
    print("your list: ",lst)
    print("list after rotation \n",rotatelist(lst,int(k)))
    ch=input("Continue (y/n)?")
