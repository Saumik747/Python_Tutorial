"""Practical 13:
Write a python program to read item information (id, name, price, qty)
in file “item.dat”.
Write a menu driven program to perform the following operations
using Random access file.
1)	Search for specific item by name.
2)	Find costliest item.
3)	Display all item and total cost.
"""
ch="y"
while ch=="y":
         print("Select appropriate option")
         print("1. Search for specific item")
         print("2. Find the costliest Item")
         print("3. Display All items and total cost")
         otp=int(input("Enter choice"))
         def DisplayAll():
                  f1=open("D:\python savefile\practicals\item.dat","r")
                  print(f1.read())
                  f1=open("D:\python savefile\practicals\item.dat","r")
                  x=True
                  sum1=0
                  while x:
                           f2=f1.readline()
                           if not f2:
                                    x=False
                           else:
                                    l1=[]
                                    l1=f2.split(",")
                                    sum1+=int(l1[2])
                  print("Total price of all items: ",sum1)
                  f1.close()
         def dall():
             f1=open("D:\python savefile\practicals\item.dat","r")
             a=[]
             b=[]
             x=[]
             y=[]
             r=True
             s=input("enter item to be searched")
             while r:
                 f2=f1.readline()
                 if not f2:
                     r=False
                 else:
                     l1=[]
                     l1=f2.split(",")
                     x.append(l1)
             
             
             for i in range(0,len(x)):
                 for j in range(0,len(x[i])):
                     if s in x[i]:
                         print(x[i],end=" ")
                         break
         
         
                 
         def CostliestItems():
                  f1=open("D:\python savefile\practicals\item.dat","r")
                  x=True
                  y=[]
                  max1=0
                  while x:
                           f2=f1.readline()
                           if not f2:
                                    x=False
                           else:
                                    l1=[]
                                    l1=f2.split(",")
                                    y.append(l1)
                                    if(int(l1[2])>max1):
                                             max1=int(l1[2])
                          
                  print("Costliest Item is : - ",max1)
                  
                  for i in range(0,len(y)):
                      for j in range(0,len(y[i])):
                          if str(max1) in y[i]:
                              print(y[i],end=" ")
                              break
                                     
                  
                                   
             
                 
                  
                                    
         
         if(otp==1):
             dall()
         
         elif(otp==2):
             CostliestItems()
        
         elif(otp==3):
             DisplayAll()
             
         
         
         ch=input("\n Do you wish to continue (y/n)?")
