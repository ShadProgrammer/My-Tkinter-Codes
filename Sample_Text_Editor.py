from tkinter import *

root = Tk()
root.geometry('870x290')
root.minsize(870, 290)
root.maxsize(870, 290)

root.title("Dweep Text Editor")

frame1 = Frame(root,bg = "Black", borderwidth=10)
frame1.grid(sticky="nw",padx=50)                    # giving padx for making space for bitmaps

b1 = Button(frame1, text = "File", bg = "Black", fg = "grey", font = "algerian 12")
b1.grid(row=0 , column=0, sticky="e")

space = Label(frame1, text = "             ", bg = "Black")
space.grid(row=1 , column=0 , sticky="w")

title = Label(frame1, text = "Your files:-             ", bg = "Black", fg = "lime", font = "algerian 12")
title.grid(row=2 , column=0 , sticky="w")

b3 = Button(frame1, text = "Password Manager.txt", bg = "Black", fg = "lime", font = "algerian 12")
b3.grid(row=3 , column=0 , sticky="w")

b4 = Button(frame1, text = "Tkinter_Practice.py", bg = "Black", fg = "lime", font = "algerian 12")
b4.grid(row=4 , column=0, sticky="w")

b5 = Button(frame1, text = "Sample_Text_Editor.py", bg = "Black", fg = "lime", font = "algerian 12")
b5.grid(row=5 , column=0, sticky="w")

space = Label(frame1, text = "      ", bg = "Black")
space.grid(row=2 , column=1 , sticky="w")                   # Space between 'file' and 'edit'

b6 = Button(frame1, text = "Edit", bg = "Black", fg = "grey", font = "algerian 12")
b6.grid(row=0 , column= 2)

space = Label(frame1, text = "      ", bg = "Black")
space.grid(row=2 , column=3 , sticky="w")                   # Space between 'edit' and 'selection'

b7 = Button(frame1, text = "Selection", bg = "Black", fg = "grey", font = "algerian 12")
b7.grid(row=0 , column=4)

space = Label(frame1, text = "      ", bg = "Black")        # Space between 'selection' and 'view'
space.grid(row=2 , column=5 , sticky="w")

b8 = Button(frame1, text = "View", bg = "Black", fg = "grey", font = "algerian 12")
b8.grid(row=0, column=6)

space = Label(frame1, text = "      ", bg = "Black")        # Space between 'view' and 'go'
space.grid(row=2 , column=7 , sticky="w")

b9 = Button(frame1, text = "Go", bg = "Black", fg = "grey", font = "algerian 12")
b9.grid(row=0, column=8)

space = Label(frame1, text = "      ", bg = "Black")        # Space between 'go' and 'run'
space.grid(row=2 , column=9 , sticky="w")

b10 = Button(frame1, text = "Run", bg = "Black", fg = "grey", font = "algerian 12")
b10.grid(row=0, column=10)

space = Label(frame1, text = "      ", bg = "Black")        # Space between 'run' and 'terminal'
space.grid(row=2 , column=11 , sticky="w")

b11 = Button(frame1, text = "Terminal", bg = "Black", fg = "grey", font = "algerian 12")
b11.grid(row=0, column=12)

space = Label(frame1, text = "      ", bg = "Black")        # Space between 'terminal' and 'help'
space.grid(row=2 , column=13 , sticky="w")

b12 = Button(frame1, text = "Help", bg = "Black", fg = "grey", font = "algerian 12")
b12.grid(row=0, column=14)

frame2 = Frame(root, bg = "black", borderwidth=5)           # 2nd Frame for bitmaps at 'nw' side
frame2.grid(row=0,column=0,sticky="nw")

b14 = Button(frame2, bitmap="question",border=12, bg="red")
b14.grid(row=0 , column=0)

b15 = Button(frame2, bitmap="questhead",border=12, bg="red")
b15.grid(row=1 , column=0)

b16 = Button(frame2, bitmap="info",border=12, bg="red")
b16.grid(row=2 , column=0)

b17 = Button(frame2, bitmap="warning",border=12, bg="red")
b17.grid(row=3 , column=0)

b18 = Button(frame2, bitmap="hourglass",border=12, bg="red")
b18.grid(row=4 , column=0)

b19 = Button(frame2, bitmap="gray50",border=12, bg="red")
b19.grid(row=5 , column=0)

root.mainloop()
# Menu widget required to decorate it more beautifully
