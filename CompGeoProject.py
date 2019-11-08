###Monotone Chain Algorithm Visualization Using Turtles###

#Function to make random points
import random
def Randompoints(start, end, num) :
    points = []
    for i in range(num):
        points.append((random.randint(start,end),random.randint(start,end)))
    return points

#Convex Hull Visualizer Function
#p,u,l,f,t are all turtles
def convex_hull_visualize(points,p,u,l,f,t):

    #Points are sorted by x coordinate using built in 'sorted' function and sets
    points = sorted(set(points)) 
    
    #Plot all points in the window
    for i in points:
        p.penup()
        p.goto(i)
        p.pendown()
        p.stamp()

    if len(points)<= 1:    #trivial Case where we only have 1 point
        return points

    #2D Cross product!
    def cross(o,a,b):
        return(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    
    #Returns positive if counter-clockwise
    #Returns negative if clockwise
    #Returns 0 if points are collinear


    #Build lower hull
    lower = []
    i=0         #index for how many points are currently in the hull
    for p in (points):
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: #If not a counter clockwise turn, undo turtles last two movements and remove the last point from the hull. 
            i-=1           
            l.goto(p)
            l.undo()
            l.undo()
            lower.pop()
        lower.append(p)
        l.goto(lower[i])
        l.pendown()
        i+=1

    #Build upper hull
    upper = []
    j=0
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1],p) <= 0:
            j-=1
            u.goto(p)
            u.undo()
            u.undo()
            upper.pop()
        upper.append(p)
        u.goto(upper[j])
        u.pendown()
        j+=1

    #Combination of both lists is the convex hull
    #Last point lower hull list is removed because it is repeated at the beginning of the upper hull list   
    Hull = lower[:-1] + upper

    #Create final convex hull and write coordinates
    for i in Hull:
        f.goto(i)
        t.goto(i)
        t.stamp()
        f.pendown()
        t.write(str(i),False,align="right",font = ("System", 13, "bold"))
        
#create turtles and visualize 
def create_hull(canvas):
    #Ask user for number of points in the plane and speed of visualization
    POINTS = int(canvas.textinput("Points","Enter # of points:"))
    SPEED = int(canvas.textinput("Speed","Enter Visualization Speed 1-10:")) 

    #Create turtle to place points
    p = turtle.RawTurtle(canvas)
    p.color('pink')
    p.shape('circle')
    p.shapesize(.35,.35)
    p.speed(0)

    #Create turtle for upper hull (blue)
    u = turtle.RawTurtle(canvas)
    u.hideturtle()
    u.color('blue')
    u.speed(SPEED)
    u.pensize(3)
    u.penup()

    #Create turtle for lower hull (purple)
    l = turtle.RawTurtle(canvas)
    l.hideturtle()
    l.color('purple')
    l.speed(SPEED)
    l.pensize(3)
    l.penup()

    #Create Turtle for writing hull coordinates
    t = turtle.RawTurtle(canvas)
    t.hideturtle()
    t.color('red')
    t.fillcolor('black')
    t.shape('circle')
    t.speed(0)
    t.shapesize(.4,.4)
    t.pensize(4)
    t.penup()

    #Final Hull turtle
    f=turtle.RawTurtle(canvas)
    f.hideturtle()
    f.color('light green')
    f.speed(8)
    f.pensize(4)
    f.penup()

    #Visualize
    convex_hull_visualize(Randompoints(-300,300,POINTS),p,u,l,f,t)

#Create window for drawing turtles
import turtle 
import tkinter as tk
win = tk.Tk()
win.configure(background = 'black')
win.title('Monotone Chain Convex Hull Visualizer')
canvas = tk.Canvas(win,bg='black', width = 750, height = 675)
canvas.pack()
turtle_window=turtle.TurtleScreen(canvas)
turtle_window.bgcolor('black')

#Reset window and start new hull function
def Reset():
    turtle_window.reset()
    create_hull(turtle_window)

#Create new hull button
reset_window_button = tk.Button(win,text = 'CREATE CONVEX HULL',fg='light green',bg='grey', width = 45,font = ("System", 13, "bold"))
reset_window_button.pack()
reset_window_button['command'] = Reset

#First call when user first runs program 
#create_hull(turtle_window)

win.mainloop()






