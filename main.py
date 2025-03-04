import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t = turtle.Turtle()
t.setheading(45)
t.speed(1)


t.pencolor('brown')
t.fillcolor('brown')
t.begin_fill()
t .forward(45)
t .right(90)
t .forward(45)
t .right(90)
t .forward(45)
t .right(90)
t .forward(45)
t .right(90)
t.end_fill()

t.setheading(135)
t.pencolor('cyan')
t.fillcolor('cyan')
t.begin_fill()
t .forward(45)
t .left(90)
t .forward(45)
t .left(90)
t .forward(45)
t .left(90)
t .forward(45)
t .left(90)
t.end_fill()

turtle.done()

