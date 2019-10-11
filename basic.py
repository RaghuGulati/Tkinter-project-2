# Tkinter-project-2
from tkinter import *
master = Tk()
master.title("Basic")

y=""

def prtx():
	y = t.get("1.0","end-1c")
	l = Label(master,text=y,width=10) 
	l.grid(row=4)

def prtl():
	y = t.get("1.0","end-1c")
	l = Label(master, text=len(y), width=10)
	l.grid(row=4)

t=Text(master,height=2,width=5)
t.grid(row=0)
    
b2=Button(master,text="print_string",command=lambda: prtx())
b2.grid(row=2)

b1=Button(master,text="print_length",command=lambda: prtl())
b1.grid(row=3)

l2 = Label(master,text="Output",width=10)
l2.grid(row=4)

mainloop()
