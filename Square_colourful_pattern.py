from tkinter import *
from time import sleep
from random import choice, randint

root = Tk()
root.geometry("1500x1000")
root.title("Chess design")
root.configure(bg= "black")
colors = ("red", "blue", "lime", "cyan","green", "magenta", "yellow", "orange", "black", "white", "violet", 'pink',"brown")
color = choice(colors)
value= randint(50,60)

def loops1(num):
    for j in range(10):
        square = Label(bitmap= "error", fg= color, bg= color,bd= 10, width= value, height= value)
        square.grid(row= j, column= j+(num))

def loops2(num):
    for j in range(10):
        square = Label(bitmap= "error", fg= color, bg= color,bd= 10, width= value, height= value)
        square.grid(row= j+(num), column= j)

# while True:
for digit in range(1,10):
    color = choice(colors)
    for i in range(0,20,2):
        root.update_idletasks()
        loops2(i)
        sleep(0.1)
        loops1(i)
        sleep(0.1)
    color = choice(colors)
    for i in range(1,20,1):
        root.update_idletasks()
        loops2(i)
        sleep(0.1)
        loops1(i)
        sleep(0.1)

root.mainloop()