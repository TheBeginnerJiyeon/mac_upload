import turtle
import random

# 거북이 만나면 꼬리 하나 늘어가기 spot_lists, random_lists
# 점수 더하면서 거북이 없애기  turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Catch Turtle")
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

spot_lists=[[None] * 16 for _ in range(16)]
for j in range(0,16):
    for k in range(0,16):
        spot_lists[j][k]=[start_center_x+j*square_size,start_center_y-k*square_size]   

print(spot_lists)

random_lists=[]
# prey turtle
def prey_turtle():    
    j=random.randint(0,15)
    k=random.randint(0,15)
    l=spot_lists[j][k]
    random_lists.append(l)

    # prey turtle random distribution
    prey_t=turtle.Turtle()
    prey_t.shape("turtle")
    prey_t.left(45)
    prey_t.color("green")
    prey_t.penup()
    screen.tracer(0)
    prey_t.goto(l[0],l[1])
    prey_t.pendown()
    screen.tracer(1)
    return prey_t
    
prey_t1=prey_turtle()
print(random_lists)
        
# moving turtle shape and size control
move_t=board_turtle.clone()
move_t.color("lightblue")
board_turtle.hideturtle()
move_t.shape("square")
move_t.shapesize(square_size/20,square_size/20)
move_t.pen(pendown=False)
move_t.speed(1)


#  chess board coordinate
value=[30*i-225 for i in range(16)]
print(value)

current_action=None
move_t2=None

# Define functions to change direction
def move_up():
    global current_action
    global move_t2
    current_action="Up"
    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Up" and move_t.position()[1]<=225:
        for i in range(current_y_num,16,1):    
            move_t.goto(value[current_x_num],value[i])
            if list(move_t.position()) in random_lists:
                move_t2=another_turtle(move_t.position()[0],move_t.position()[1])
                random_lists.remove(list(move_t.position()))
                if list(prey_t1.position()) not in random_lists:
                    prey_t1.clear()
                    prey_t1.hideturtle()
            if move_t2!=None and i>0:
                move_t2.goto(value[current_x_num],value[i-1])
                move_t2.speed(1)
                
                

            
    return 0
        


def move_right():
    global current_action
    global move_t2
    current_action="Right"

    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Right" and move_t.position()[0]<=225:
        for i in range(current_x_num,16,1):    
            move_t.goto(value[i],value[current_y_num])
            if list(move_t.position()) in random_lists:
                move_t2=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                if list(prey_t1.position()) not in random_lists:
                    prey_t1.clear()
                    prey_t1.hideturtle()
            if move_t2!=None and i>0:
                move_t2.goto(value[i-1],value[current_y_num])
                move_t2.speed(1)
                


    return 0
    
def move_down():
    global current_action
    global move_t2
    current_action="Down"

    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Down" and move_t.position()[1]>=-225:
        for i in range(current_y_num,-1,-1):    
            move_t.goto(value[current_x_num],value[i])
            if list(move_t.position()) in random_lists:
                move_t2=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                if list(prey_t1.position()) not in random_lists:
                    prey_t1.hideturtle()
                    prey_t1.clear()
            if move_t2!=None and i<15:
                move_t2.goto(value[current_x_num],value[i+1])
                move_t2.speed(1)
                

    return 0
    

def move_left():
    global current_action
    global move_t2
    current_action="Left"
        
    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Left" and move_t.position()[0]>=-225:
        for i in range(current_x_num,-1,-1):    
            move_t.goto(value[i],value[current_y_num])
            if list(move_t.position()) in random_lists:
                move_t2=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                if list(prey_t1.position()) not in random_lists:
                    prey_t1.hideturtle()
                    prey_t1.clear()
            if move_t2!=None and i<15:
                move_t2.goto(value[i+1],value[current_y_num])
                move_t2.speed(1)
                
    
    return 0



# Bind keyboard events to functions
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")

# moving turtle animation

def another_turtle(x,y):
    move_t2=move_t.clone()
    move_t2.color("blue")

    move_t2.pen(pendown=False)
    move_t2.speed(1)

    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))
    move_t2.setposition(value[current_x_num],value[current_y_num])
    return move_t2

# score



# Listen for keyboard events
screen.listen()

# Keep the window open
screen.mainloop()
