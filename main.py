import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Checkered Board")
screen.tracer(0)  # Turn off animation

# Create a turtle
board_turtle = turtle.Turtle()
board_turtle.speed(0)  # Set the fastest drawing speed

# Define the size of each square and the number of rows and columns
square_size = 30
rows = 8
columns = 8

# Function to draw a single row of squares
def draw_row(color1, color2):
    for _ in range(columns):
        draw_square(color1)
        draw_square(color2)

# Function to draw a single square
def draw_square(color):
    board_turtle.begin_fill()
    board_turtle.fillcolor(color)
    for _ in range(4):
        board_turtle.forward(square_size)
        board_turtle.right(90)
    board_turtle.end_fill()
    board_turtle.penup()
    board_turtle.forward(square_size)
    board_turtle.pendown()

start_x=(-columns * square_size)
start_y=((screen.window_height())/2-square_size)

start_center_x=start_x+square_size/2
start_center_y=start_y-square_size*1.5

# Function to draw the entire checkered board
def draw_board():
    colors = ["black", "white"]
    board_turtle.goto(start_x,start_y)
    for i in range(16):
        color1 = colors[i % 2]
        color2 = colors[(i + 1) % 2]
        board_turtle.penup()
        board_turtle.goto(start_x, board_turtle.ycor() - square_size)
        board_turtle.setheading(0)
        board_turtle.pendown()
        draw_row(color1, color2)

# Draw the board
board_turtle.penup()
board_turtle.goto(-columns * square_size / 2, rows * square_size / 2)

draw_board()


board_turtle.penup()
board_turtle.color("pink")
board_turtle.goto(start_center_x,start_center_y)
board_turtle.pendown()

# Update the screen and animation began
screen.update()
screen.tracer(1)

spot_lists={}
prey_num=5

for i in range(prey_num):
    j=random.randint(0,15)
    k=random.randint(0,15)
    l=[start_center_x+j*square_size,start_center_y-k*square_size]
    spot_lists[f"prey_t{i}"]=l

    # prey turtle random distribution
    prey_t=turtle.Turtle()
    prey_t.shape("turtle")
    prey_t.color("green")
    prey_t.penup()
    screen.tracer(0)
    prey_t.goto(l[0],l[1])
    prey_t.pendown()
    screen.tracer(1)

print(spot_lists)


    


# moving turtle shape and size control
move_t=board_turtle.clone()
move_t.color("lightblue")
board_turtle.hideturtle()
move_t.shape("square")
move_t.shapesize(square_size/20,square_size/20)
move_t.pen(pendown=False)
move_t.speed(1)

# moving turtle animation
move_t.setheading(0)
move_t.forward(square_size*(columns*2-1))
move_t.right(90)
move_t.forward(square_size*(rows*2-1))
move_t.right(90)
move_t.forward(square_size*(columns*2-1))
move_t.right(90)
move_t.forward(square_size*(rows*2-1))
move_t.right(90)



""" def moving_law():
    if  """








# Keep the window open
screen.mainloop()
