#Made by: Carson White
#Due Date: 2/19/2024
#Problem # 3.8.11



import turtle

#This below sets up the screen

wn = turtle.Screen()

# This below sets up a turtle that is named Carson

Carson = turtle.Turtle()

#This below moves the turtle and draws a line for 200 units

Carson.forward(200)  

#This below turns the turtle right 144 degrees which is necessarcy for the star

Carson.right(144)    
Carson.forward(200)
Carson.right(144)
Carson.forward(200)
Carson.right(144)
Carson.forward(200)
Carson.right(144)
Carson.forward(200)
Carson.right(144)

# This below hides the turtle at the end of the drawing sequence
Carson.hideturtle()

#As there are 5 points there are 5 instances of forward movement and then turning to the right

wn.mainloop()
