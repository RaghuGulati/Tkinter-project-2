# Tkinter-project-2
from tkinter import *
master = Tk()

x="hello"

def prtx():
    y = t.get("1.0","end-1c")
    print(y)

def prtl():
    print(len(y))

t=Text(master,height=2,width=5)
t.grid(row=0)
    
b2=Button(master,text="prtx",command=lambda: prtx())
b2.grid(row=2)

b1=Button(master,text="prtl",command=lambda: prtl())
b1.grid(row=3)

mainloop()
