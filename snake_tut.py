import turtle

# Create the main turtle
main_turtle = turtle.Turtle()

# Function to create a new turtle
def create_new_turtle(x, y):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.goto(x, y)
    # Add additional configuration or actions for the new turtle if needed

# Function to move the main turtle and create a new turtle when it reaches a certain position
def move_main_turtle():
    main_turtle.forward(10)
    x, y = main_turtle.position()
    if x >= 100:  # Example condition for creating a new turtle
        create_new_turtle(x, y)
    turtle.ontimer(move_main_turtle, 100)  # Move main turtle recursively

# Start the movement of the main turtle
move_main_turtle()

# Start listening for keypresses
turtle.listen()

# Keep the window open
turtle.done()
