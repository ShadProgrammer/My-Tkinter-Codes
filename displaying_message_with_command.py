from tkinter import LEFT, StringVar, Tk, Entry, Button, Message
from tkinter.colorchooser import askcolor

window = Tk()

window.geometry("650x500")
window.resizable(False, False)

val = StringVar()

en = Entry(window,width= 35, textvariable= val, font= "cambria 18")
en.pack(pady= 10)

msg=  Message()
msg.place(relx= 0.3, rely= 0.5)         # Creating empty message box just to define it
def display():
    global msg
    # Everytime the button is clicked, old msg box will be destroyed
    if val.get() == "":
        pass                            # Avoiding empty text msg box
    elif msg.winfo_exists() == True:
        msg.destroy()                   # Empty message box will be destroyed and new will be mapped at first
        print(val.get())
        msg = Message(text= val.get(),bg= "blue", fg= "black", font= 'courier 20 ', width= 400)
        msg.place(relx= 0.2, rely= 0.5)

        
def tconfig():
    col = askcolor(title= 'Choose message text colour')
    msg.config(fg= col[-1])
    print(col[-1])
    
def bconfig():
    col = askcolor(title= 'Choose message box colour')
    if val.get() != "":
        msg.config(bg= col[-1])
        print(col[-1])

def boldy():                    # Making message bold
    msg.config(font= "courier 20 bold")

def undy():                     # Making message underlined
    msg.config(font= "courier 20 underline")

def ity():                      # Making message italic
    msg.config(font= "courier 20 italic")

display_but = Button(window, text= "Display", padx= 15, pady= 15, command= display)
display_but.place(x=50 , y=80)

config_txt_but = Button(text= 'Configure text colour', padx= 15, pady= 15, command= tconfig)
config_txt_but.place(x=225 , y=80 )

config_box_but = Button(text= 'Configure message box colour', padx= 15, pady= 15, command= bconfig)
config_box_but.place(x=425 , y= 80)

bold_but = Button(text= 'Make bold', padx= 15, pady= 15, command= boldy)
bold_but.place(x=50, y= 150)

und_but = Button(text= "Make underlined", padx= 15, pady= 15, command= undy)
und_but.place(x= 225, y= 150)

ita_but = Button(text= "Make italic", padx= 15, pady= 15,command= ity)
ita_but.place(x= 425, y= 150)
# However user cannot make text bold, italic and underlined at once

window.mainloop()
# Displaying configured text again will reset back to the blue~black theme