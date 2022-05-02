from tkinter import *

root = Tk()
root.resizable(False, False)
root.geometry("850x650")
root.config(bg="magenta")
root.title("Moving Stickman on the field")

can = Canvas(root, width= 850, height= 550) 
can.pack(side= TOP)

# Creating a field
grass_field = can.create_rectangle(0,0,850,550, fill= "green")
# pond = can.create_oval(110,360,670,500, fill= "blue")

# Creating road
road = can.create_rectangle(0,50,850,150, fill= "black")
# Creating road strips
strip = can.create_rectangle(10,90,50,100, fill = "white")
strip = can.create_rectangle(100,90,150,100, fill = "white")
strip = can.create_rectangle(200,90,250,100, fill = "white")
strip = can.create_rectangle(300,90,350,100, fill = "white")
strip = can.create_rectangle(400,90,450,100, fill = "white")
strip = can.create_rectangle(500,90,550,100, fill = "white")
strip = can.create_rectangle(600,90,650,100, fill = "white")
strip = can.create_rectangle(700,90,750,100, fill = "white")
strip = can.create_rectangle(800,90,850,100, fill = "white")

# Creating func. that makes stickman
def stickman(a,b,c,d,head_color= "cyan",body_color= 'blue'):        
    head = can.create_oval(a,b,c,d, fill= head_color)
    body = can.create_line(a+15,b+30,c-15,d+43, fill= body_color)   
    hands = can.create_line(a,b+50,c-15,d, fill= body_color)
    hands = can.create_line(a+30,b+50,c-15,d, fill= body_color)
    legs = can.create_line(a,b+100,c-15,d+40, fill= body_color)
    legs = can.create_line(a+30,b+100,c-15,d+40, fill= body_color)       # All maths with the help of matrices

# TOP LEFT width & height and BOTTOM RIGHT width & height should have difference of 30  

def position(event):        # Func which creates the stickman wherever user wants
    pos1 = event.x
    pos2 = event.y
    print(f"width is {pos1} and height is {pos2}")
    stickman(pos1,pos2,pos1+30,pos2+30)

can.bind("<Button-1>",position)            # Binding canvas widget with event

Label(text= "Left click of the mouse anywhere on image to create your own stickman.", font= "algerian 15 bold").pack(pady= 27)

root.mainloop()
# No restart button which can destroy all stickmans and restart the window.