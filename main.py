import turtle
import random

# 뱀 꼬리 부분 움직임만 수정하면 끝!!

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Catch Turtle")
prey_num=int(screen.numinput("Prey number","How many prey turtle?",1,1,10))
heart_color=screen.textinput("Color","what color do you like?").lower().strip()
screen.tracer(0)  # Turn off animation


# Create a turtle
board_turtle = turtle.Turtle()
board_turtle.speed(0)  # Set the fastest drawing speed

# Define the size of each square and the number of rows and columns
square_size = 30
rows = 8
columns = 8

# Function to draw a single row of squares
def draw_row(turtle,color1, color2):
    for _ in range(columns):
        draw_square(turtle,color1)
        draw_square(turtle,color2)

# Function to draw a single square
def draw_square(turtle,color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(square_size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(square_size)
    turtle.pendown()

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
        draw_row(board_turtle,color1, color2)






# Draw the board
board_turtle.penup()
board_turtle.goto(-columns * square_size / 2, rows * square_size / 2)
draw_board()
board_turtle.penup()
board_turtle.goto(start_center_x,start_center_y)
board_turtle.pendown()
board_turtle.hideturtle()





# score
score=0
score_t=turtle.Turtle()
score_t.penup()
score_t.hideturtle()
screen.tracer(0)
score_t.goto(243,-260)
score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")
score_t.pendown()
screen.tracer(1)

# Update the screen and animation began
screen.update()
screen.tracer(1)

spot_lists=[[None] * 16 for _ in range(16)]
for j in range(0,16):
    for k in range(0,16):
        spot_lists[j][k]=[start_center_x+j*square_size,start_center_y-k*square_size]   



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

prey_tn={}
for i in range(prey_num):
    prey_tn[f"prey_t{i}"]=prey_turtle()


        
# moving turtle shape and size control
move_t=turtle.Turtle()
move_t.color("lightblue")
move_t.shape("square")
move_t.shapesize(square_size/20,square_size/20)
move_t.pen(pendown=False)
move_t.speed(1)
move_t.penup()
move_t.goto(start_center_x,start_center_y)



def pink_heart():
    global heart_color
    default_color="pink"
    heart_t=turtle.Turtle()
    heart_t.hideturtle()
    
    heart_coor=[[7,8],[8,9],[9,8],[10,9],[11,8],[10,7],[9,6],[8,7]]
    heart_t.speed(0)
    for coor in heart_coor:
        heart_t.penup()
        heart_t.goto(-240+30*coor[0],-210+30*coor[1])
        try:
            draw_square(heart_t,heart_color)
        except:
            draw_square(heart_t,default_color)
        


#  chess board coordinate
value=[30*i-225 for i in range(16)]

# global variable for moving function
current_action=None
move_tn={}


# Define functions to change direction
def move_up():
    global move_t
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Up"
    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Up" and move_t.position()[1]<=225:
        for i in range(current_y_num,16,1):    
            move_t.goto(value[current_x_num],value[i])
            
            n=score

            # 꼬리가 길어져서 꼬리가 다 넣어지지 않는 길이면 하나하나 이동을 안하고 그거리를 뛰어넘어 가버린다 여기 고치기
            if list(move_t.position()) in random_lists:
                move_tn[f"move_t{n+2}"]=another_turtle(move_t.position()[0],move_t.position()[1])
                random_lists.remove(list(move_t.position()))
                score=score+1
                score_t.clear()
                score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                if score==prey_num:
                    love_turtle()
                    pink_heart()

                for prey in prey_tn:
                    if list(prey_tn[prey].position()) not in random_lists:
                        prey_tn[prey].hideturtle()

            # 뱀의 움직임을 생각해야한다
            if move_tn!={} and i>n:
                screen.tracer(0)
                for k in range(len(move_tn)):
                    move_tn[f"move_t{k+2}"].goto(value[current_x_num],value[i-(k+1)])
                screen.tracer(1)     
                            
    return 0
        


def move_right():
    global move_t
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Right"

    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Right" and move_t.position()[0]<=225:
        for i in range(current_x_num,16,1):    
            move_t.goto(value[i],value[current_y_num])

            n=score

            if list(move_t.position()) in random_lists:
                move_tn[f"move_t{n+2}"]=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                score=score+1
                score_t.clear()
                score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                if score==prey_num:
                    love_turtle()
                    pink_heart()

                for prey in prey_tn:
                    if list(prey_tn[prey].position()) not in random_lists:
                        prey_tn[prey].hideturtle()

            if move_tn!={} and i>n:
                screen.tracer(0)
                for k in range(len(move_tn)):
                    move_tn[f"move_t{k+2}"].goto(value[i-(k+1)],value[current_y_num])
                screen.tracer(1)        
    return 0
    
def move_down():
    global move_t
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t
    current_action="Down"

    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Down" and move_t.position()[1]>=-225:
        for i in range(current_y_num,-1,-1):    
            move_t.goto(value[current_x_num],value[i])
            n=score
            if list(move_t.position()) in random_lists:
                move_tn[f"move_t{n+2}"]=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                score=score+1
                score_t.clear()
                score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                if score==prey_num:
                    love_turtle()
                    pink_heart()

                for prey in prey_tn:
                    if list(prey_tn[prey].position()) not in random_lists:
                        prey_tn[prey].hideturtle()
    
            if move_tn!={} and i<(15-n):
                screen.tracer(0)
                for k in range(len(move_tn)):
                    move_tn[f"move_t{k+2}"].goto(value[current_x_num],value[i+(1+k)])
                screen.tracer(1)            

    return 0
    

def move_left():
    global move_t
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Left"
        
    current_x_num=int((move_t.position()[0]+225)//(30))
    current_y_num=int((move_t.position()[1]+225)//(30))

    while current_action=="Left" and move_t.position()[0]>=-225:
        for i in range(current_x_num,-1,-1):    
            move_t.goto(value[i],value[current_y_num])
            n=score
            if list(move_t.position()) in random_lists:
                move_tn[f"move_t{n+2}"]=another_turtle(move_t.position()[0],move_t.position()[1])
                
                random_lists.remove(list(move_t.position()))
                score=score+1
                score_t.clear()
                score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")
                if score==prey_num:
                    love_turtle()
                    pink_heart()

                for prey in prey_tn:
                    if list(prey_tn[prey].position()) not in random_lists:
                        prey_tn[prey].hideturtle()

            if move_tn!={} and i<(15-n):
                screen.tracer(0)
                for k in range(len(move_tn)):
                    move_tn[f"move_t{k+2}"].goto(value[i+(1+k)],value[current_y_num])
                screen.tracer(1)   
             
    return 0



# Bind keyboard events to functions
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")

# moving turtle animation

def another_turtle(current_x,current_y):
    move_tn=move_t.clone()
    move_tn.color("blue")

    move_tn.pen(pendown=False)
    move_tn.speed(1)

    current_x_num=int((current_x+225)//(30))
    current_y_num=int((current_y+225)//(30))
    move_tn.setposition(value[current_x_num],value[current_y_num])
    return move_tn

def love_turtle():
    love_t=turtle.Turtle()
    love_t.penup()
    love_t.hideturtle()
    screen.tracer(0)
    love_t.goto(-243,-260)
    love_t.write(f"Do you want to go out with me tonight? *^^*",font=("Arial",15,"bold"),align="left")
    love_t.pendown()
    screen.tracer(1)

# Listen for keyboard events
screen.listen()

    
# Keep the window open
screen.mainloop()


# 문제 없음
print(move_tn)
print(random_lists)
print(score)
