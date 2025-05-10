import turtle

t = turtle.Turtle()
t.width(10)

# Draw square
for i in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(180, 0)
t.pendown()

#Draw a hexagon
for i in range(6):
    t.forward(100)
    t.right(60)

t.hideturtle()
turtle.done()
