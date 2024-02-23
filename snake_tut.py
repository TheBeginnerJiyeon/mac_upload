import turtle

def draw_square(turtle,color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

t=turtle.Turtle()
screen=turtle.Screen()
heart_color=screen.textinput("Color","what color do you like?").lower().strip()
print(heart_color)

def pink_heart():
    global heart_color
    default_color="pink"
    heart_t=turtle.Turtle()
    heart_t.hideturtle()
    heart_t.penup()
    heart_coor=[[7,8],[8,9],[9,8],[10,9],[11,8],[10,7],[9,6],[8,7]]
    heart_t.speed(0)
    for coor in heart_coor:
        heart_t.penup()
        heart_t.goto(-240+30*coor[0],-210+30*coor[1])
        try:
            draw_square(heart_t,heart_color)
        except:
            draw_square(heart_t,default_color)

pink_heart()

turtle.done()