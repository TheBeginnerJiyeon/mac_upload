import turtle

# Create a turtle object
t = turtle.Turtle()
t.forward(100)

t2 =turtle.Turtle()

t2.goto(t.position())

turtle.done()