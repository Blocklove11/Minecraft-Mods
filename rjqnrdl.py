import turtle

turtle.bgcolor(0.5, 0.1, 0.3)#1=100%, Bgcolor
turtle.color(1,1,1)#거북거북거북이 색깔
turtle.shape('turtle')
turtle.shapesize(2, 2, 1)#(가로, 세로, 선두께)
turtle.speed(0)
def move_right():
    turtle.setheading(0)#거북거북거북이 머리방향
    turtle.fd(10)
def move_left():
    turtle.setheading(180)
    turtle.fd(10)
def move_up():
    turtle.setheading(90)
    turtle.fd(10)
def move_down():
    turtle.setheading(270)
    turtle.fd(10)
turtle.onkey(move_right,'Right')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.listen()


