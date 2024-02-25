import turtle
import random


# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Catch Turtle")
prey_num=int(screen.numinput("Prey number","How many prey turtle?",1,1,10))
heart_color=screen.textinput("Color","what color do you like?").lower().strip()
screen.tracer(0)  # Turn off animation


# Create a turtle
board_turtle = turtle.Turtle()
board_turtle.hideturtle()
board_turtle.speed(0)  # Set the fastest drawing speed

# Define the size of each square and the number of rows and columns
square_size = 30
rows = 8
columns = 8

# Function to draw a single row of squares
def draw_row(turtle,color1, color2):
    turtle.hideturtle()
    for _ in range(columns):
        draw_square(turtle,color1)
        draw_square(turtle,color2)

# Function to draw a single square
def draw_square(turtle,color):
    turtle.hideturtle()
    turtle.pendown()
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
    board_turtle.hideturtle()
    board_turtle.goto(start_x,start_y)
    for i in range(16):
        color1 = colors[i % 2]
        color2 = colors[(i + 1) % 2]
        board_turtle.hideturtle()
        board_turtle.penup()
        board_turtle.goto(start_x, board_turtle.ycor() - square_size)
        board_turtle.setheading(0)
        board_turtle.pendown()
        draw_row(board_turtle,color1, color2)

# Draw the board
board_turtle.hideturtle()
board_turtle.penup()
board_turtle.goto(-columns * square_size / 2, rows * square_size / 2)
draw_board()
board_turtle.penup()
board_turtle.goto(start_center_x,start_center_y)
board_turtle.pendown()


# score
score=0
score_t=turtle.Turtle()
score_t.hideturtle()
score_t.penup()
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

    while True:
        j=random.randint(0,15)
        k=random.randint(0,15)
        l=spot_lists[j][k]
        if l not in random_lists:
            random_lists.append(l)
            break
        else:
            continue

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
move_t1=turtle.Turtle()
move_t1.color("lightblue")
move_t1.shape("square")
move_t1.shapesize(square_size/20,square_size/20)
move_t1.pen(pendown=False)
move_t1.speed(1)
move_t1.penup()
move_t1.goto(start_center_x,start_center_y)


def pink_heart():
    global heart_color
    default_color="pink"
    heart_t=turtle.Turtle()
    heart_t.hideturtle()
    heart_t.penup()
    heart_crd=[[7,8],[8,9],[9,8],[10,9],[11,8],[10,7],[9,6],[8,7]]
    heart_t.speed(0)
    for crd in heart_crd:
        heart_t.hideturtle()
        heart_t.penup()
        heart_t.goto(-240+30*crd[0],-210+30*crd[1])
        if heart_color=="":
            draw_square(heart_t,default_color)
        else:
            try:
                draw_square(heart_t,heart_color)
            except:
                draw_square(heart_t,default_color)
            

        

#  chess board coordinate
value=[30*i-225 for i in range(16)]

# global variable for moving function
current_action=None
move_tn={"move_t1":move_t1}


# 움직임 함수 다 다시 쓰기
def move_up():
    global move_t1
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Up"
    current_x_num=int((move_t1.position()[0]+225)//(30))
    current_y_num=int((move_t1.position()[1]+225)//(30))
    move_t1.goto(value[current_x_num],value[current_y_num])
    move_t1.setheading(90)
    n=score

    # 먹이 숨기기
    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()

    for _ in range(15):
        while current_action=="Up" and move_t1.position()[1]<=225:        
            if current_action!="Up":
                break
            # 꼬리 갯수만 고치면!!!!!! ㅠㅠ

            copy_position=[]
            for index,key in enumerate(move_tn):
                copy_position.append(move_tn[key].position())

            for index,key in enumerate(move_tn):    
                if index>=1:
                    move_tn[key].goto(copy_position[index-1])       

            if move_t1.position()[1]==225:
                if move_t1.position()[0]==-225:
                    move_t1.right(90)
                elif move_t1.position()[0]==225:
                    move_t1.left(90)
                else:
                    move_t1.right(90)                         
                
                move_t1.forward(square_size)

        

                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()                           

            else:
                move_t1.forward(square_size)
                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()

                 

def move_right():
    global move_t1
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Right"
    current_x_num=int((move_t1.position()[0]+225)//(30))
    current_y_num=int((move_t1.position()[1]+225)//(30))
    move_t1.goto(value[current_x_num],value[current_y_num])
    move_t1.setheading(0)
    n=score

    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()

    for _ in range(15):
        while current_action=="Right" and move_t1.position()[0]<=225:
            if current_action!="Right":
                break     

            copy_position=[]
            for index,key in enumerate(move_tn):
                copy_position.append(move_tn[key].position())

            for index,key in enumerate(move_tn):    
                if index>=1:
                    move_tn[key].goto(copy_position[index-1])       

            if move_t1.position()[0]==225:
                if move_t1.position()[1]==-225:
                    move_t1.left(90)
                elif move_t1.position()[1]==225:
                    move_t1.right(90)
                else:
                    move_t1.right(90)                         
                
                move_t1.forward(square_size)

                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()                           

            else:
                move_t1.forward(square_size)
                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()

                 

def move_down():
    global move_t1
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Down"
    current_x_num=int((move_t1.position()[0]+225)//(30))
    current_y_num=int((move_t1.position()[1]+225)//(30))
    move_t1.goto(value[current_x_num],value[current_y_num])
    move_t1.setheading(270)
    n=score

    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()

    for _ in range(15):
        while current_action=="Down" and move_t1.position()[1]>=-225: 
            if current_action!="Down":
                break         
                    
            copy_position=[]
            for index,key in enumerate(move_tn):
                copy_position.append(move_tn[key].position())

            for index,key in enumerate(move_tn):    
                if index>=1:
                    move_tn[key].goto(copy_position[index-1])  

            if move_t1.position()[1]==-225:
                if move_t1.position()[0]==-225:
                    move_t1.left(90)
                elif move_t1.position()[0]==225:
                    move_t1.right(90)
                else:
                    move_t1.right(90)                         
                
                move_t1.forward(square_size)

                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    

                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()                           

            else:
                move_t1.forward(square_size)
                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()

                 
def move_left():
    global move_t1
    global current_action
    global move_tn
    global prey_tn
    global score
    global score_t

    current_action="Left"
    current_x_num=int((move_t1.position()[0]+225)//(30))
    current_y_num=int((move_t1.position()[1]+225)//(30))
    move_t1.goto(value[current_x_num],value[current_y_num])
    move_t1.setheading(180)
    n=score

    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()

    for _ in range(15):
        while current_action=="Left" and move_t1.position()[0]>=-225:
            if current_action!="Left":
                break         
            
            copy_position=[]
            for index,key in enumerate(move_tn):
                copy_position.append(move_tn[key].position())

            for index,key in enumerate(move_tn):    
                if index>=1:
                    move_tn[key].goto(copy_position[index-1])  

            if move_t1.position()[0]==-225:
                if move_t1.position()[1]==-225:
                    move_t1.right(90)
                elif move_t1.position()[1]==225:
                    move_t1.left(90)
                else:
                    move_t1.right(90)                         
                
                move_t1.forward(square_size)

                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])
                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()                           

            else:
                move_t1.forward(square_size)
                if list(move_t1.position()) in random_lists:
                    score_t.clear()
                    move_tn[f"move_t{n+2}"]=another_turtle(move_tn[f"move_t{n+1}"].position()[0],move_tn[f"move_t{n+1}"].position()[1])

                    random_lists.remove(list(move_t1.position()))
                    score=score+1
                    
                    score_t.write(f"Score: {score}",font=("Arial",20,"bold"),align="right")

                    if score==prey_num:
                        love_turtle()
                        pink_heart()
                        return 0

                    for prey in prey_tn:
                        if list(prey_tn[prey].position()) not in random_lists:
                            prey_tn[prey].hideturtle()
    


# Bind keyboard events to functions
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")

# moving turtle animation

def another_turtle(current_x,current_y):
    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()
    
    move_trail=turtle.Turtle()
    move_trail.hideturtle()
    screen.tracer(0)
    move_trail.penup()
    move_trail.shape("square")
    move_trail.color("blue")
    move_trail.shapesize(square_size/20,square_size/20)
    move_trail.speed(1)
    current_x_num=int((current_x+225)//(30))
    current_y_num=int((current_y+225)//(30))
    move_trail.setposition(value[current_x_num],value[current_y_num])
    move_trail.showturtle()
    screen.tracer(1)

    return move_trail

def love_turtle():
    love_t=turtle.Turtle()
    love_t.penup()
    love_t.hideturtle()
    screen.tracer(0)
    love_t.goto(-243,-260)
    love_t.write(f"Do you want to go out with me tonight? *^^*",font=("Arial",15,"bold"),align="left")
    love_t.pendown()
    screen.tracer(1)

    for prey in prey_tn:
        if list(prey_tn[prey].position()) not in random_lists:
            prey_tn[prey].hideturtle()

# Listen for keyboard events
screen.listen()

    
# Keep the window open
screen.mainloop()


print(score)
print(random_lists)
print(move_tn)
