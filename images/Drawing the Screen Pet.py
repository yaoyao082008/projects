import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(10)
t.penup()
t.goto(-20, -200)
t.pendown()

#Drawing the head
for i in range(36):
    t.forward(30)
    t.left(10)

#Drawing the Nose
t.penup()
t.goto(-20, -60)
t.pendown()

t.setheading(0)

for i in range(5):
    t.forward(25)
    t.right(120)
starting_nose_x = t.xcor()
starting_nose_y = t.ycor()

#Drawing the Whiskers
t.left(120)
t.forward(10)
for i in range(4):
    t.right(16)
    t.forward(17)

t.penup()
t.goto(starting_nose_x, starting_nose_y)
t.pendown()
t.setheading(-60)

t.forward(10)
for i in range(4):
    t.left(16)
    t.forward(17)
   
#Drawing the Eyes
t.penup()
t.goto(-80, -10)
t.pendown()

t.left(90)
for i in range(90):
    t.forward(2)
    t.right(4)

t.penup()
t.goto(40, 20)
t.pendown()

t.left(-90)
for i in range(90):
    t.forward(2)
    t.right(4)

#Drawing the Eyeballs
t.penup()
t.goto(-60, -10)
t.pendown()

t.left(90)
for i in range(90):
    t.forward(2)
    t.right(12)

t.penup()
t.goto(40, 0)
t.pendown()

t.left(-90)
for i in range(90):
    t.forward(2)
    t.right(12)

#Drawing the Mouth
t.penup()
t.goto(-40, -110)
t.pendown()
t.right(100)
for i in range(10):
    t.forward(12)
    t.left(21)

t.penup()
t.goto(50, 135)
t.pendown()
t.forward(100)
t.left(120)
t.forward(110)
