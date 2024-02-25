import turtle

# Create a turtle object
t = turtle.Turtle()

t.setheading(270)

# Rotate the turtle to the right by 90 degrees
t.right(90)
score=1
t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")
t.clear()

turtle.done()