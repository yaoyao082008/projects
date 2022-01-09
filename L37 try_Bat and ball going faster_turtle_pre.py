import random
import turtle as t

t.bgcolor('dodgerblue4')
canvasWidth=750
canvasHeight=500
canvas = t.Screen()
canvas.screensize(canvasWidth, canvasHeight)

left_wall=-t.window_width()/2
right_wall=t.window_width()/2
top_wall=t.window_height()/2
bottom_wall=-t.window_height()/2

bat=t.Turtle()
bat.shape('square')
bat.shapesize(1,3,1)
bat.color('dark turquoise')
bat.speed(0)
bat.penup()
bat.goto(0,bottom_wall+50)

ball=t.Turtle()
ball.shape('circle')
ball.color('deep pink')
ball.speed(0)
ball.penup()

score = 0
showScore=t.Turtle()
showScore.hideturtle()
showScore.speed(0)
def display_score(score):
    global left_wall, right_wall, top_wall
    showScore.clear()
    showScore.penup()
    x=right_wall-50
    y=top_wall-50
    showScore.setpos(x,y)
    showScore.write('Score:'+str(score),align='right',font=('Courier',15))

bounceCount = 0
level=1
showLevel=t.Turtle()
showLevel.hideturtle()
showLevel.speed(0)
def display_level(score):
    global left_wall, right_wall, top_wall
    showLevel.clear()
    showLevel.penup()
    x=left_wall+100
    y=top_wall-50
    showLevel.setpos(x,y)
    showLevel.write('level:'+str(level),align='right',font=('Courier',15))
    
   
    
            
batSpeed = 20        
def move_bat_left():
    global batSpeed, left_wall
    bat.speed(batSpeed)
    (batX, batY) = bat.pos()
    if batX>left_wall:
        bat.backward(batSpeed)        
    
def move_bat_right():
    global batSpeed, right_wall
    bat.speed(batSpeed)
    (batX, batY) = bat.pos()
    if  batX<right_wall:
        bat.forward(batSpeed)
    

def start_game():
    global x,ballSpeed, ballHeading, score,bounceCount,level, batSpeed,ball_bounce,bat_length
    ball_bounce=0
    bat_length=0
    x=3
    ball.goto(0,0)
    ballSpeed = 10
    ballHeading = random.randrange(40,75)
    score = 0
    level=1
    display_score(score)
    display_level(level)

    while True:
        ball.setheading(ballHeading)
        ball.forward(ballSpeed)
        (ballX, ballY) = ball.pos()
        (batX, batY) = bat.pos()
        if ballX > right_wall-15:
            ballHeading = 180-ballHeading
            ball.setheading(ballHeading)
            ball_bounce+=1
            bat_length+=1
        if ballX < left_wall+15:
            ballHeading = 180-ballHeading
            ball.setheading(ballHeading)
            ball_bounce+=1
            bat_length+=1
        if ballY > top_wall-15 :
            ballHeading = -ballHeading
            ball.setheading(ballHeading)
            ball_bounce+=1
            bat_length+=1
#        if ball.distance(bat)<20:
        if ballY < batY+5 and ballX>batX-30 and ballX<batX+30 :
            ballHeading = -ballHeading
            ball.setheading(ballHeading)
            score = score + 1
            display_score(score)
            ball_bounce+=1
            bat_length+=1
        if ball_bounce==4:
            ballSpeed+=1
            ball_bounce=0
            level+=1
            display_level(level)
        if bat_length==8:
            x= x+1
            bat.shapesize(1,x,1)
            bat_length==0
            
        if ballY < bottom_wall:
            print("Your score was " + str(score))
            break
        
t.onkey(start_game,'space')
t.onkey(move_bat_left, 'Left')
t.onkey(move_bat_right, 'Right')
t.listen()
t.mainloop()


