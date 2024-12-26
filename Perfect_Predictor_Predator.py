from tkinter import *
from random import randint
from tkinter import messagebox as msg

root = Tk()
root.geometry("550x450")
# root.resizable(False, False)
root.config(bg= "orange")

def clear_widg():                           # This func. will destroy all widgets of the current screen
    lst1 = root.pack_slaves()         # root.slaves() doesn't works for all so it's better
    lst2 = root.place_slaves()        # to use slaves func. with specific method !
    lst = lst1 + lst2
    for i in lst:
        # print(i)
        i.destroy()

life = 5

def game(game_mode):
    clear_widg()
    l1 = Label(text= "Guess the number x", bg= "orange", fg= "purple", font= "algerian 30")
    l1.pack(side= TOP, pady= 22)

    if game_mode.upper() == "EASY":
        x = randint(1,50)
        print(x)
        s = Spinbox(width= 10, from_= 1, to= 50, font= "algerian 20")
        s.pack(pady= 22)
    elif game_mode.upper() == "MEDIUM":
        x = randint(1,100)
        print(x)
        s = Spinbox(width= 10, from_= 1, to= 100, font= "algerian 20")
        s.pack(pady= 22)
    elif game_mode.upper() == "HARD":
        x = randint(1,1000)
        print(x)
        s = Spinbox(width= 10, from_= 1, to= 1000, font= "algerian 20")
        s.pack(pady= 22)
        
    l2 = Label(bg= "orange", fg= "white", font= "algerian 20")      # Creating empty label
    l2.pack()       
    l3 = Label(bg= "orange", text=  f"{life} life remaining", fg= "blue", font= "algerian 20")
    l3.pack()

    def check():
        global life
        if int(s.get()) == x:
            # print("Excellent")
            l2.config(text= "Well Done! You guessed it correct.", fg= "green")
            submit.config(state= DISABLED)
        elif int(s.get()) < x:
            # print("Need higher number")
            l2.config(text= "Need higher number, Try again!")
            life -= 1
            
        elif int(s.get()) > x:
            # print("Need lower number")
            l2.config(text= "Need lower number, Try again!")
            life -= 1
        # print(s.get(), f"life : {life}")

        if life <= 0:
            submit.config(state= DISABLED)
            l2.config(text= "0 life, You lose!", fg= 'red')

        l3.config(text= f"{life} life remaining")

    submit = Button(text= "Check", bg= "black", fg= "cyan", font= "algerian 15", command= check)
    submit.pack(pady=30)

    def quitgame():
        choice = msg.askyesno("Confirmation", "Are you sure you want to quit your current game? You won't be able to continue your game further.")
        if choice == True:
            clear_widg()
            begin()

    go_back = Button(text= "Quit", bg= "black", fg= "red", font= "algerian 20", command= quitgame) 
    go_back.pack()

def easy():
    clear_widg()
    game("easy")

def medium():
    clear_widg()
    game("medium")

def hard():
    clear_widg()
    game("hard")

def survival():
    clear_widg()

def back():
    clear_widg()
    begin()

def init():
    clear_widg()
    lives = 5
    Button(text= "Back", padx= 50, bg= "purple", font= "chiller 20 bold", fg= "black", pady= 3, command= back).pack(side= BOTTOM, pady= 15)
    Button(text= "Survival", padx= 50, bg= "purple", font= "chiller 20 bold", fg= "black", pady= 3, command= survival).pack(side= BOTTOM, pady= 15)
    Button(text= "Hard", padx= 50, bg= "purple", font= "chiller 20 bold", fg= "black", pady= 3, command= hard).pack(side= BOTTOM, pady= 15)
    Button(text= "Medium", padx= 50, bg= "purple", font= "chiller 20 bold", fg= "black", pady= 3, command= medium).pack(side= BOTTOM, pady= 15)
    Button(text= "Easy", padx= 50, bg= "purple", font= "chiller 20 bold", fg= "black", pady= 3, command= easy).pack(side= BOTTOM, pady= 15)

def instructions():
    clear_widg()
    def getback():
        clear_widg()
        begin()             # Packs back all widgets of main menu

    txt = '''Hello Welcome to Perfect Predictor Predator game.\n 
  1. This game is very simple. So you don't need any tutorial/instructions for it.
  2. Just try to guess the number x before you run out of your all lives.
  3. There are 4 modes in this games :- Easy ; No. can be 1 to 50, Medium :- No. can be 1 to 100, Hard :- No. can be 
     1 to 1000, Survival :- Contains unlimited levels -- Check yourself how much can you clear without losing lives
  4. You'll regain your life in each new level in survival mode.
  5. You can change number of lives and many more things from top menu. '''

    m = Message(width= 470, text= txt, font= "courier 13", bg= 'orange', fg= "maroon")
    m.pack(pady= 7, anchor= NW)
    Button(text= "Okay, got it!", bg= 'black', fg= 'lime', font= "chiller 18", command= getback).pack(side= BOTTOM, pady= 8)

def credits():
    clear_widg()
    def getback():
        clear_widg()
        begin()                     # packs back all widgets of main menu

    c = '''This game is made by a Python Programmer, Dweep Bariya. \n1) Nested functions, \n2) Tkinter module, \n3) Random module
are used in making this game. It took around 2 days to put an cherry on the cake.\n
    Thank You, I hope you enjoyed my Perfect Predictor Predator Python game.'''

    Message(width= 550, text= c, font= "courier 13", bg= "orange", fg= "maroon").pack(pady= 8)

    Button(text= "Okay", bg= "black", fg= "lime", font= "chiller 18", padx= 30, command= getback).pack(side= BOTTOM, pady= 7)
    

# Main window buttons inside begin function to reuse it whenver back button is pressed 
def begin():
    Label(text= "Perfect Predictor Predator", font= "chiller 44 underline bold", fg= 'blue', bg= 'orange').pack(pady= 33)

    Button(text= "More about this game",padx= 60,bg= "purple", font= "chiller 20 bold", command= credits).pack(pady= 15, side= BOTTOM)

    Button(text= "How to play",padx= 60,bg= "purple", font= "chiller 20 bold", command= instructions).pack( pady= 15, side= BOTTOM)

    Button(text= "Play", padx= 60, bg= "purple", font= "chiller 20 bold", command= init).pack( pady= 15, side= BOTTOM)

begin()

root.mainloop()