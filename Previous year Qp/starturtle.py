import turtle

screen=turtle.Screen()
screen.bgcolor("white")

star=turtle.Turtle()
star.color("black")
star.home()
star.pensize(2)
star.speed(2)

for i in range(5):
    star.forward(100)
    star.right(144)

star.hideturtle()
turtle.done()

