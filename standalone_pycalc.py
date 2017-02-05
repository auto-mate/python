#standalone calc
# Use Tkinter for python 2, tkinter for python 3

#import tkinter        (access classes A B C by tkinter.A tkinter.B tkinter.C)
#import tkinter as x   (access classes A B C by x.A x.B x.C)
#from tkinter import * (access classes A B C by A B C)

from tkinter import * # one is func
from tkinter import messagebox as mb
import tkinter as tk  # one is class    



def mFEq():
    calcStr=StringVar()
    calcStr=mVar.get()
    #remove last 2 characters (print(calcStr[:-2]))
    calcVal=eval(calcStr)
    mVar.set(calcVal)

def mF1():
    mVar.set("A Test String")

def mF2():
    mVar.set(mNewText.get())
    return

def mF3():
    pass

def mF4():
    mVar.set("A Test String")

def mFMn():
    mVar.set("A Test String")

def mFClear():
    mVar.set("")
   
def mFAdd(No):
    mVal= mVar.get()
    mVar.set(mVal+No)

def fQuit():
    mOk =  mb.askyesno(title="Exit",message="Are you sure?")
    if mOk != 0:
        root.destroy()        
    return
	
def fAbout():
    mb.showinfo(title="About pyCalc",message="A Simple Calculator Made in Python3\n By Andrew Harper :-)")

#Make Window
root=tk.Tk()
root.title("PY Calc")

#Menu
root.myMenuBar = tk.Menu()

root.myTopItem = tk.Menu(root.myMenuBar)
root.myTopItem.add_command(label="Quit",command=fQuit,underline=0)
root.myTopItem.add_command(label="About pyCalc",command=fAbout,underline=0)

root.myMenuBar.add_cascade(label="Options",menu=root.myTopItem,underline=0)

root.config(menu=root.myMenuBar)

#Draw and Size
root.grid()
root.geometry('220x300+200+200')

mVar=StringVar()
mVar.set("0")

c1=10
c2=60
c3=110
c4=160

rm1=240
r0=190
r1=140
r2=90
r3=40

#Answer Bar
root.myLabelResult=tk.Label(root,textvariable=mVar,anchor=tk.E,fg="#000000",bg="#ffffff",bd="1",font="-family arial -size 14 -overstrike 0 -underline 0 -slant roman")
root.myLabelResult.place(x=10, y=5, height=30, width=200)

#Row0
root.myButton_00=tk.Button(root,text="0",width=2,command=lambda xNo="0":mFAdd(xNo),fg="black")
root.myButton_00.place(x=c1, y=r0, height=50, width=50)

myButton_Pt=Button(root,text=".",width=2,command=lambda xNo=".":mFAdd(xNo),fg="black")
myButton_Pt.place(x=c2, y=r0, height=50, width=50)
    
myButton_Eq=Button(root,text="=",width=2,command=mFEq,bg="lightgreen", fg="black")
myButton_Eq.place(x=c3, y=r0, height=50, width=50)

myButton_Pl=Button(root,text="+",width=2,command=lambda xNo="+":mFAdd(xNo),fg="black")
myButton_Pl.place(x=c4, y=r0, height=50, width=50)

#Row1
myButton_01=Button(root,text="1",width=2,command=lambda xNo="1":mFAdd(xNo),fg="black")
myButton_01.place(x=c1, y=r1, height=50, width=50)

myButton_02=Button(root,text="2",width=2,command=lambda xNo="2":mFAdd(xNo),fg="black")
myButton_02.place(x=c2, y=r1, height=50, width=50)
    
myButton_03=Button(root,text="3",width=2,command=lambda xNo="3":mFAdd(xNo),fg="black")
myButton_03.place(x=c3, y=r1, height=50, width=50)

myButton_Mn=Button(root,text="-",width=2,command=lambda xNo="-":mFAdd(xNo),fg="black")
myButton_Mn.place(x=c4, y=r1, height=50, width=50)

#Row2
myButton_04=Button(root,text="4",width=2,command=lambda xNo="4":mFAdd(xNo),fg="black")
myButton_04.place(x=c1, y=r2, height=50, width=50)

myButton_05=Button(root,text="5",width=2,command=lambda xNo="5":mFAdd(xNo),fg="black")
myButton_05.place(x=c2, y=r2, height=50, width=50)
    
myButton_06=Button(root,text="6",width=2,command=lambda xNo="6":mFAdd(xNo),fg="black")
myButton_06.place(x=c3, y=r2, height=50, width=50)

myButton_Tm=Button(root,text="x",width=2,command=lambda xNo="*":mFAdd(xNo),fg="black")
myButton_Tm.place(x=c4, y=r2, height=50, width=50)

#Row3
myButton_07=Button(root,text="7",width=2,command=lambda xNo="7":mFAdd(xNo),fg="black")
myButton_07.place(x=c1, y=r3, height=50, width=50)

myButton_08=Button(root,text="8",width=2,command=lambda xNo="8":mFAdd(xNo),fg="black")
myButton_08.place(x=c2, y=r3, height=50, width=50)
    
myButton_09=Button(root,text="9",width=2,command=lambda xNo="9":mFAdd(xNo),fg="black")
myButton_09.place(x=c3, y=r3, height=50, width=50)

myButton_Dv=Button(root,text="/",width=2,command=lambda xNo="/":mFAdd(xNo),fg="black")
myButton_Dv.place(x=c4, y=r3, height=50, width=50)

###Row-1
myButton_Cl=Button(root,text="Clear",width=2,command=mFClear,bg="orange",fg="black")
myButton_Cl.place(x=c1, y=rm1, height=40, width=200)

root.mainloop()
