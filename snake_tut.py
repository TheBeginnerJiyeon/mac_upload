import turtle

# Set up the screen
screen = turtle.Screen()



# Set the turtle pen to draw in "square" mode
turtle.pen(pendown=False, pencolor="black", pensize=20, resizemode="auto")

# Set the turtle shape to "square"
turtle.shape("square")

# Your drawing code here
# For example:
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# Keep the window open
turtle.done()



