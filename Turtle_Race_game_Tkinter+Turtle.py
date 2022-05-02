from tkinter import BOTTOM, NW, W, Entry, Frame, Label, StringVar, Tk, Button, Message
import turtle as t
from random import randint
from tkinter.messagebox import showerror

mainwindow = Tk()
mainwindow.config(bg= "maroon")
mainwindow.title("Turtle Racing game")
mainwindow.geometry("650x500")
mainwindow.resizable(False, False)

def clear_widg():                           # This func. will destroy all widgets of the current screen
    lst1 = mainwindow.pack_slaves()         # mainwindow.slaves() doesn't works for all so it's better
    lst2 = mainwindow.place_slaves()        # to use slaves func. with specific method !
    lst = lst1 + lst2
    for i in lst:
        # print(i)
        i.destroy()

def playwindow():                           # When Single Player is clicked this func will be called
    # turtle racting game func.
    # tur1 - tur6 are racers and player1 - player6 are each racers name
    def game(tur1, tur2, tur3, tur4, tur5, tur6, player1, player2, player3, player4, player5, player6):
        s = t.Screen()
        s.screensize(canvwidth= 800, bg= "grey")
        
        # Making finish line 
        f = t.Turtle()
        f.ht()
        f.up()
        f.pen(speed= 0, pensize= 3)
        f.setpos(250,250)
        f.down()
        f.rt(90)
        f.fd(500)

        # Making Turtle Racers
        x,y = -300,50
        t1 = t.Turtle("turtle")
        t1.up()
        t1.shapesize(1.5,1.5,1.5)
        t1.color(tur1, tur1)
        t1.goto(x,y+200)
        t1.down()
        t2 = t.Turtle("turtle")
        t2.up()
        t2.shapesize(1.5,1.5,1.5)
        t2.color(tur2, tur2)
        t2.goto(x,y+100)
        t2.down()
        t3 = t.Turtle("turtle")
        t3.up()
        t3.shapesize(1.5,1.5,1.5)
        t3.color(tur3, tur3)
        t3.goto(x,y)
        t3.down()
        t4 = t.Turtle("turtle")
        t4.up()
        t4.shapesize(1.5,1.5,1.5)
        t4.color(tur4, tur4)
        t4.goto(x,y-100)
        t4.down()
        t5 = t.Turtle("turtle")
        t5.up()
        t5.shapesize(1.5,1.5,1.5)
        t5.color(tur5, tur5)
        t5.goto(x,y-200)
        t5.down()
        t6 = t.Turtle("turtle")
        t6.up()
        t6.shapesize(1.5,1.5,1.5)
        t6.color(tur6, tur6)
        t6.goto(x,y-300)
        t6.down()

        turtles = (t1, t2, t3, t4, t5, t6)          # Racers tuple
        Players = (player1, player2, player3, player4, player5, player6)    # turtle names tuple
        flag = 0
        lst = []
        def move_turtle(turtle,txt):
            nonlocal flag, lst            
            if turtle.pos() <= (250,250) and txt not in lst:
                turtle.write(arg= txt, font= "chiler 25 bold", move= False)
                turtle.fd(randint(10,50))
                # Appending text into list so this if statement will run only once for all texts
                lst.append(txt)                 
                
            elif turtle.pos() <= (250,250):         # if txt in lst, this elif statement will run
                turtle.fd(randint(10,50))
            
            elif turtle.pos() >= (235,250) and flag == 0:   # First turtle completes the race will be enlarged
                turtle.shapesize(3,3,3)
                flag += 1

        for k in range(25):                     # All turtles will try to move 25 steps
            for i in range(6):                  # This will move each turtle one by one 
                move_turtle(turtles[i], Players[i])

        t.exitonclick()
    
    
    # Function which will initialise the game... Making this func. to avoid use of lambda in button command
    def init():
        try:
            game(col1.get(), col2.get(), col3.get(), col4.get(), col5.get(), col6.get(), pal1.get(),pal2.get(),pal3.get(),pal4.get(),pal5.get(),pal6.get())              # Posititonal arguments
        except t.TurtleGraphicsError:       # avoiding invalid colour names
            showerror("Colour error", "You entered invalid colour name somewhere. Please check back again.")
            t.clear()
            t.bye()
        except TypeError:           # Unexpected errors in this game
            showerror("Oops", "Unexpected Error occured!")
            t.clear()
            t.bye()
        except t.Terminator:
            pass                # Double click next time to run turtle GUI

    # Back button func clears all widg. of current screen and packs previous screen's widg.
    def back_button():
        clear_widg()
        begin()         # Packs back all main menu widgets

    # Clearing all widgets of mainmenu ~~~ Single Player, Credits and Help button
    clear_widg()

    Button(text= "<---", command= back_button, font= "chiller 10 bold",bg= "black",fg= "white", padx= 20).pack(anchor= NW, pady= 5, padx= 5)

    fr1 = Frame(mainwindow)
    fr1.pack(pady= 25)

    for i in range(6):
        Label(text= f"Turtle{i+1}", font= "cambria 15", bg= "black", fg= "lime").pack(anchor= W, pady= 10, padx= 25)

    Label(text= "Turtle name", font= "chiller 25 bold underline", bg= "black", fg= "lime").place(x= 175, y= 50)
    Label(text= "Turtle colour", font= "chiller 25 bold underline", bg= "black", fg= "lime").place(x= 425, y= 50)

    places = (100,150,200,250,300,350)
    pal1, pal2, pal3, pal4, pal5, pal6 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar() 
    first_vals = (pal1, pal2, pal3, pal4, pal5, pal6)

    col1, col2, col3, col4, col5, col6 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    second_vals = (col1, col2, col3, col4, col5, col6)

    # default_nam = ("Player1","Player2","Player3","Player4","Player5","Player6")
    default_colr = ("red","green","black","yellow","navy blue","orange")

    for i in range(6):
        Entry(mainwindow, textvariable= first_vals[i], font= "curves 15", fg= "navy blue").place(x= 125, y= places[i])
        # first_vals[i].set(default_nam[i])
        Entry(mainwindow, textvariable= second_vals[i], font= "curves 15", fg= "navy blue").place(x= 375, y= places[i])
        second_vals[i].set(default_colr[i])

    # Following button triggers the game func.
    Button(text= "Ready for the Race", font= "chiller 22 bold", bg= "black", fg= "yellow", command= init, padx= 44).pack(side= BOTTOM, pady= 10)

def instructions():
    clear_widg()
    def getback():
        clear_widg()
        begin()             # Packs back all widgets of main menu

    msg = '''\t  Hello Welcome to Turtle Racing game.\n 
  1. This game is very simple. So you don't need any tutorial/instructions for it.
  2. But anyways, You can set each turtle names and play it.
  3. You can set each turtle it's own colour but make sure that you enter valid colour names.
  4. Maximum turles are 6 in this game. You cannot increase or decrease the number of turtles.
  5. If you are clicking the race button second time, you need to click the button again to make racing GUI active.
  6. Turtles move with random steps, so don't think about this game biased if only one turtle is winning game in a row. '''

    m = Message(width= 570, text= msg, font= "courier 15", bg= 'maroon', fg= "cyan")
    m.pack(pady= 7, anchor= NW)
    Button(text= "Okay, got it!", bg= 'black', fg= 'yellow', font= "chiller 22", command= getback).pack(side= BOTTOM, pady= 8)

def cred():
    clear_widg()
    def getback():
        clear_widg()
        begin()                     # packs back all widgets of main menu

    c = '''This game is made by a Python Programmer, Dweep Bariya. \n1) Nested functions, \n2) Tkinter module, \n3) Turtle module
are used in making this game. It took around 1 week to put an cherry on the cake. To be specific, I completed this
game in 8 hours(1 hr each day).\n
    Thank You, I hope you enjoyed my first Python game.'''

    Message(width= 650, text= c, font= "courier 15", bg= "maroon", fg= "lime").pack(pady= 8)

    Button(text= "Okay", bg= "black", fg= "yellow", font= "chiller 22", padx= 30, command= getback).pack(side= BOTTOM, pady= 7)

# Main window buttons inside begin function to reuse it whenver back button is pressed 
def begin():
    Label(text= "Turtle Racing Game", font= "chiller 75 underline bold", fg= 'blue', bg= 'maroon').pack(pady= 33)

    Button(text= "More about this game",padx= 60,bg= "blue", font= "chiller 22 bold", command= cred).pack(pady= 15, side= BOTTOM)

    Button(text= "How to play",padx= 60,bg= "blue", font= "chiller 22 bold", command= instructions).pack( pady= 15, side= BOTTOM)

    Button(text= "Play", padx= 60, bg= "blue", font= "chiller 22 bold", command= playwindow).pack( pady= 15, side= BOTTOM)

begin()

mainwindow.mainloop()
