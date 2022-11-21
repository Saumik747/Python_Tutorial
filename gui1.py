]\from tkinter import *
import tkinter.messagebox

gui=Tk()
def agecalc():
    res_day=Label(gui,text="Day: ")
    res_month=Label(gui,text="Month: ")
    res_year=Label(gui,text="Year: ")
    ress=Label(gui,text="YOur Age is :")
    m30=[4,6,9,11]
    m31=[1,3,5,7,8,10,12]
    m28=[2]
    mt=[1,2,3,4,5,6,7,8,9,10,11,12]
    mnt =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t1day=0


    dobday=int(dob_dd.get())
    dobmnth=int(dob_mm.get())
    dobyyyy=int(dob_yyyy.get())

    pday=int(pres_dd.get())
    pmnth=int(pres_mm.get())
    pyear=int(pres_yyyy.get())
    if(dobyyyy>=pyear):
        tkinter.messagebox.showerror("Value error","dob cannot be greater than presentday")
        
                

    elif(dobyyyy<=pyear):
        if((dobday<=31 and pday<=31)and (dobmnth in mt and pmnth in mt)):
            rday=pday-dobday
            rmnth=pmnth-dobmnth
            ryear=pyear-dobyyyy
            
                                

            if((dobday<=mnt[dobmnth])and (pday<=mnt[pmnth])):
                if(dobmnth>pmnth):
                    nmnth=12-(dobmnth-pmnth)
                    ryear=ryear-1
         
         


      
    rsd=str(rday)
    rsm=str(nmnth)
    rsy=str(ryear)
    res_dd=Label(gui,text=rsd.replace('-',''))
   
    res_mnth=Label(gui,text=rsm.replace('-',''))
    res_yyyy=Label(gui,text=rsy.replace('-',''))

    

    ress.grid(row=11,column=0)
    res_day.grid(row=12,column=0)
    res_dd.grid(row=12,column=1)

    res_month.grid(row=13,column=0)
    res_mnth.grid(row=13,column=1)

    res_year.grid(row=14,column=0)
    res_yyyy.grid(row=14,column=1)

    
    


gui.configure(background = "light blue")
gui.geometry("640x800")
gui.title("Age Calculator")
    
dob=Label(gui,text="Enter Date of Birth",bg="light green")
dob_day=Label(gui,text="Enter Day: ",bg="light green")
dob_month=Label(gui,text="Enter Month: ",bg="light green")
dob_year=Label(gui,text="Enter Year: ",bg="light green")
dob_dd=Entry(gui)
dob_mm=Entry(gui)
dob_yyyy=Entry(gui)
dob.grid(row=0, column=0)

   
    



pres_dt=Label(gui,text="Present Day",bg="orange")
pres_day=Label(gui,text="Enter Day: ",bg="orange")
pres_month=Label(gui,text="Enter Month: ",bg="orange")
pres_year=Label(gui,text="Enter Year: ",bg="orange")
pres_dd=Entry(gui)
pres_mm=Entry(gui)
pres_yyyy=Entry(gui)



dob_day.grid(row=1,column=0)
dob_dd.grid(row=1,column=1)

dob_month.grid(row=2,column=0)
dob_mm.grid(row=2,column=1)

dob_year.grid(row=3,column=0)
dob_yyyy.grid(row=3,column=1)


pres_dt.grid(row=5,column=0)
pres_day.grid(row=6,column=0)
pres_dd.grid(row=6,column=1)

pres_month.grid(row=7,column=0)
pres_mm.grid(row=7,column=1)

pres_year.grid(row=8,column=0)
pres_yyyy.grid(row=8,column=1)

resage = Button(gui, text = "Resultant Age", bg = "Red", command = agecalc)
resage.grid(row=9,column=0)




    







   

   
    




gui.mainloop()
