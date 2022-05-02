from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar

root = Tk()
root.config(bg= "grey")
root.geometry("450x300")
root.title("Get Set Go")

Label(text= "Tap to start countdown", font= "cambria 30 underline", bg= 'grey').pack(side= TOP)

l1 = Label(text= "Ready...", font= "chiller 50 bold", bg= 'grey')
l1.place(relx= 0.4, rely= 0.4)
prog = Progressbar(length= 500, mode= 'determinate', orient= VERTICAL)
prog.pack(side= RIGHT, fill= BOTH)

def lab1(event):
    prog['value'] = 0
    l1.config(text= "3", font= "chiller 50 bold", bg= 'grey')
    prog['value'] += 25
    root.after(1000, lab2)

def lab2():
    l1.config(text= "2", font= "chiller 50 bold", bg= 'grey')
    prog['value'] += 25
    root.after(1000, lab3)

def lab3():
    l1.config(text= "1", font= "chiller 50 bold", bg= 'grey')
    prog['value'] += 25
    root.after(1000, lab4)

def lab4():
    l1.config(text= "Go!!!", font= "chiller 50 bold", bg= 'grey')
    prog['value'] += 25

root.bind("<Button-1>", lab1)

root.mainloop()