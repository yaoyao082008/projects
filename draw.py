import turtle as t
from random import randint,random
def draw_star(points,size,col,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(180-180/points)
    t.end_fill()
    
def get_pos(x,y):
    ranCol=(random(),random(),random())
    ranPts=randint(2,5)*2+1
    ranSize=randint(10,50)

    draw_star(ranPts,ranSize,ranCol,x,y)
            
t.onscreenclick(get_pos)
t.Screen().bgcolor("blue")

    

