from tkinter import *


window=Tk()

def konvertuj():
    kilogrami=e1Vrednost.get()
    kilogrami=int(kilogrami)

    funteIznos=kilogrami*2.20462
    funte.insert(END, funteIznos)

    gramiIznos=kilogrami*1000
    grami.insert(END, gramiIznos)    

    unceIznos=kilogrami*35.274
    unce.insert(END, unceIznos)

b1=Button(window, text="Izvrsi", command=konvertuj)
b1.grid(row=5, column=0)
l1=Label(window, text="Konverter")
l1.grid(row=0, column=0)

l2=Label(window, text="Iznos u Kg: ")
l2.grid(row=1, column=0)

e1Vrednost=StringVar()
e1=Entry(window,textvariable=e1Vrednost, width=20)
e1.grid(row=1, column=1)


#funte
l3=Label(window, text="Funte: ")
l3.grid(row=2, column=0)

funte=Text(window, height=1, width=20)
funte.grid(row=2, column=1)

#grami

l4=Label(window, text="Grami: ")
l4.grid(row=3, column=0)

grami=Text(window, height=1, width=20)
grami.grid(row=3, column=1)

#unce
l5=Label(window, text="Unce:")
l5.grid(row=4, column=0)

unce=Text(window, height=1, width=20)
unce.grid(row=4, column=1)





window.mainloop()