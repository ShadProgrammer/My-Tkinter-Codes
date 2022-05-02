from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.config(bg= 'navy blue')
root.geometry("550x650")

val1 = StringVar()
val2 = StringVar()

fr = Frame(bg= 'green')
fr.grid(padx= 20, pady= 250, ipady= 30)

Label(fr, text= 'Enter your first name', font= 'cambria 15').grid(row= 0, column= 0, padx= 15, pady= 10)
Entry(fr, textvariable= val1).grid(row= 0, column= 1, padx= 15, pady= 10, sticky= W)

Label(fr, text= 'Enter your last name', font= 'cambria 15').grid(row= 1, column= 0, padx= 15, pady= 10)
Entry(fr, textvariable= val2).grid(row= 1, column= 1, padx= 15, pady= 10, sticky= W)

Label(fr, text= 'Enter your gender', font= 'cambria 15').grid(row= 2, column= 0, padx= 15, pady= 10)
opt = Combobox(fr, width=20)
opt['value'] = ("Select", "Male", "Female", "Others", "Don't want to tell")
opt.current(0)
opt.grid(row= 2, column= 1, sticky= W)

Label(fr, text= 'Enter your profile description', font= 'cambria 15').grid(row= 3, column= 0, padx= 15, pady= 10)
Text(fr, height= 3, width= 30, font= "cambria 10").grid(row= 3, column= 1, sticky= W)

def clear_window():
    first_name = val1.get()
    last_name = val2.get()
    gender = opt.grab_release()     
    print(first_name, last_name, gender)
    fr.destroy()
    b1.destroy()
    new()
    

b1 = Button(root, text= "Submit", font= 'curve 18 bold',bg= 'black',fg= 'yellow', command= clear_window)
b1.place(relx= 0.4, rely= 0.8)

def new():
    Label(text= f"Welcome {val1.get() + val2.get()}", font= "cambria 25 bold", bg= 'navy blue', fg= 'white').pack(anchor= CENTER, pady= 280)

root.mainloop()