from tkinter import *
# from tkinter.ttk import *
from tkinter import colorchooser as ch

window = Tk()
window.config(bg= 'green')
window.geometry("650x500")
window.title("Your TODO task list box")
color1 = "white" ; color2 = "black" ; color3 = "white" ; color4 = "black"
# scroll = Scrollbar(window)
# scroll.pack(side = RIGHT, fill= Y)        # Adding scrollbar is remaining

def head(master):
    header = Label(master, text= "Your today's task list", bg= color1, fg= color2, font= "algerian 25 underline", pady= 6)
    header.pack(side= TOP, fill= X)

def main(master):
    subjects = ("Science", "Maths", "History", "Geography", "Hindi","Sanskrit")
    fontstyle = "cambria 15"
    Label(master, text= "Your school works: ", font= "cambria 20 bold italic").pack(anchor= "nw", pady= 10)
    for i in range(6):
        Checkbutton(master, text= subjects[i], font= fontstyle, bg= color3, fg= color4).pack(anchor= "nw" , padx= 66, pady= 3)

    works = ("Cleaning the house", "Mopping the floor", "Washing utensils", "Washing clothes")
    Label(master, text= "Your house works: ", font= "cambria 20 bold italic").pack(anchor= "nw", pady= 15)
    for i in range(4):
        Checkbutton(master, text= works[i], font= fontstyle, bg= color3, fg= color4).pack(anchor= "nw" , padx= 66, pady= 3)

# scroll.config(window.yview)
head(window)
main(window)

def color(section):
    colourbox = ch.askcolor()
    print(colourbox[-1])                # It's a tuple and I only need colour code
    return colourbox[-1]

mainmenu = Menu(window, tearoff= 0)
submenu = Menu(mainmenu, tearoff= 0)
mainmenu.add_cascade(label= "Colour settings",menu= submenu)
subsubmenu= Menu(submenu, tearoff= 0) 
submenu.add_cascade(label= "Configure colour",menu= subsubmenu)
subsubmenu.add_command(label= "Change header background colour", command= lambda: color(head))
subsubmenu.add_command(label= "Change main slide background colour", command= lambda: color(main))
window.config(menu= mainmenu)

window.mainloop()