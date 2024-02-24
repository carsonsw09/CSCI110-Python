# Made by Carson White
# Due Date: 2/26/2024
# Problem # 4.9.2

def main():
    pass

if '_name_' == '_main_': 
    main()
    



import turtle

def draw_square(t):
     """Make turtle t draw a square of sz."""
     size = 20 # Sets the initial size of the sides
     
     for a in range(5): # There are 5 squares so the for loop iterates through 5 times
        t.penup()
        t.backward(10)  
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
        
        # The logic above moves the pen without drawing 10 to the left and 10 down from the final corner
        # on the initial square. The pen will move before drawing, but this only impacts the starting position
        # of the square
        
        # The loop below then operates 4 times to make the 4 sides of the square
        
        for i in range(4):
            t.forward(size+20*a)
            t.left(90)
         
         
         


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()      # Create alex
draw_square(alex)       # Call the function to draw the square
wn.mainloop()