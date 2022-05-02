from tkinter import *

x = y = 0
# Using random module and globalising x,y inside function so that value of x and y 
# changes everytime the button gets clicked 
def randomania():                           
    global x,y
    from random import randint
    x = randint(1,100)
    y = randint(1,100)

def add():                                          # For button 1
    global x,y
    randomania()
    print(f"Addition of {x} and {y} is {x + y}")

def minus():                                            # For button 2
    global x,y
    randomania()
    print(f"Subtraction of {x} and {y} is {x - y}")

def mult():                                          # For button 3
    global x,y
    randomania()
    print(f"Multiplication of {x} and {y} is {x * y}")

def div():                                          # For button 4
    global x,y
    randomania()
    print(f"Division of {x} and {y} is {x / y}")


root = Tk()
root.geometry("650x500")
root.minsize(600,500)                   # width, height

root.title("---4 Buttons with different command---")

header = Label(text = "Click on following buttons to see operations on random numbers :)", fg = 'red',font=(None,15))
header.pack(side = TOP)

frame1 = Frame(root,bg='purple',borderwidth=35)
frame1.pack(pady=150)

button1 = Button(frame1,text = "Addition", bg = 'cyan', fg = 'brown', command = add)
button1.pack()

button2 = Button(frame1,text = "Subtraction", bg = 'lime', fg = 'brown', command = minus)
button2.pack()

button1 = Button(frame1,text = "Multiplication", bg = 'yellow', fg = 'brown', command = mult)
button1.pack()

button1 = Button(frame1,text = "Division", bg = 'pink', fg = 'brown', command = div)
button1.pack()

root.mainloop()
