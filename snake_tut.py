import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Drawing")
screen.tracer(0)  # Turn off animation

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.hideturtle()  # Hide the turtle arrow

# Example drawing
t.penup()
t.goto(-100, 0)
t.pendown()
for _ in range(4):
    t.forward(200)
    t.left(90)

# Update the screen
screen.update()

# Keep the window open
screen.mainloop()

