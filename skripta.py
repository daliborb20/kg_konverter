from tkinter import *


window = Tk()

def exe():
    kilometri=e1Vrednost.get()
    kilometri=int(kilometri)
    milje=kilometri*1.6
    t1.insert(END, milje)
    return milje

b1=Button(window,text="Izvrsi", command=exe)
b1.grid(row=0, column=0)

e1Vrednost=StringVar()
e1=Entry(window, textvariable=e1Vrednost)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)










window.mainloop()