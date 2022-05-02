from tkinter import *
from random import choice

window = Tk()
window.title("Trolling Om GUI")
window.geometry("875x600")
window.resizable(False, False)

Label(window, text= "Click anywhere in blue box to display a message containing OM in it.", font= "algerian 18").pack()

can = Canvas(window, width= 800, height = 550, bg= "navy blue")

om_list = ["I am OM-ELET", "I am M-OM-ENTUM", "I am RAND-OM", "I am R-OM", "I am RAND-OM-ACCESS MEMORY"]

def om1(event):
    can.create_text(event.x, event.y, text= choice(om_list), fill= 'white', font= "courier 15 bold underline")

can.bind("<Button-1>", om1)
can.pack()

# Why adding a button disables my canvas widget? Whatever method I use to pack
# button=  Button(window, text= "Clear window", font= "cambria 12 bold", padx= 10, pady= 5, command= can.destroy())
# button.place(relx= 0.5, rely= 0.873)

window.mainloop()