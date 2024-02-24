import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    # Below is a set of if-else statements that will take in
    # the height value and then figure out the corresponding fill color
    # for that bar on the graph
    
    if height > 200:
        t.color("blue", "red")  
    elif height > 100:
        t.color("blue", "yellow")  
    else:
        t.color("blue", "green")  
    
    t.begin_fill()  
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()  
    t.forward(10)

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,52,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
