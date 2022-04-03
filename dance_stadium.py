import pgzrun
from random import randint
HEIGHT=600
WIDTH=800
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
move_list=[]
display_list=[]
score=0
current_move=0
count=4
dance_length=4
level=0

say_dance=False
show_countdown=True
game_over=False
moves_complete=False

dancer=Actor("dancer-start")
dancer.pos=CENTER_X,CENTER_Y-30
right=Actor("right")
right.pos=CENTER_X+60,CENTER_Y+170
up=Actor("up")
up.pos=CENTER_X-10,CENTER_Y+100
left=Actor("left")
left.pos= CENTER_X-80,CENTER_Y+170
down=Actor("down")
down.pos=CENTER_X-10,CENTER_Y+240
def draw():
    screen.clear()
    screen.blit("stage",(0,0))
    dancer.draw()
    right.draw()
    up.draw()
    left.draw()
    down.draw()
    if show_countdown:
        screen.draw.text("%s" %str(count), color="black", center=(CENTER_X,CENTER_Y-130),fontsize=60)
    if say_dance:
        screen.draw.text("DANCE!", color="black", center=(CENTER_X,CENTER_Y-130),fontsize=60)
    screen.draw.text("Score: %s" %score, color="black", center=(CENTER_X+300,CENTER_Y-200),fontsize=30)
def reset():
    
    up.image="up"
    dancer.image="dancer-start"
    down.image="down"
    right.image="right"
    left.image="left"
      
def update_dancer(move):
    global game_over
    if not game_over:
        if move==0:
            up.image="up-lit"
            dancer.image="dancer-up"
            clock.schedule(reset,0.3)
        elif move==1:
            down.image="down-lit"
            dancer.image="dancer-down"
            clock.schedule(reset,0.3)
        elif move==-1:
            right.image="right-lit"
            dancer.image="dancer-right"
            clock.schedule(reset,0.3)
        elif move==-2:
            left.image="left-lit"
            dancer.image="dancer-left"
            clock.schedule(reset,0.3)
            
def countdown():
    global count
    if count>0:
        count-=1
        clock.schedule(countdown,1)
    else:
        show_countdown=False
        display_moves()
    return
def display_moves():
    global move_list, display_list, dance_length, say_dance, show_countdown, current_move
    if display_list:
        this_move=display_list.pop(0)
        if this_move==0:
            update_dancer(0)
            clock.schedule(display_moves,1)
        elif this_move==1:
            update_dancer(1)
            clock.schedule(display_moves,1)
        elif this_move==-1:
            update_dancer(-1)
            clock.schedule(display_moves,1)
        elif this_move==-2:
            update_dancer(-2)
            clock.schedule(display_moves,1)

    else:
        say_dance=True
        show_countdown=False
    return

            
def on_key_up(key):
    global score, game_over,move_list,current_move
    print(move_list)
    if key==keys.UP:
        update_dancer(0)
        if move_list[current_move]==0:
            print("up")
            score+=1
            next_move()
        else:
            game_over=True
    if key==keys.DOWN:
        update_dancer(1)
        if move_list[current_move]==1:
            score+=1
            next_move()
        else:
            game_over=True
    if key==keys.RIGHT:
        print("right")
        update_dancer(-1)
        if move_list[current_move]==-1:
            score+=1
            next_move()
        else:
            game_over=True
    if key==keys.LEFT:
        update_dancer(-2)
        if move_list[current_move]==-2:
            score+=1
            next_move()
        else:
            game_over=True
       
    return

def next_move():
    global dance_length,current_move,moves_complete
    print("nextmove")
    if current_move<dance_length-1:
        
        current_move+=1
        print(current_move)
    else:
        moves_complete=True
        print("movecomplete",current_move)
    return




def generate_moves():
    global move_list, display_list, dance_length, count, show_countdown, say_dance
    dance_length=dance_length+level
    count=4
    move_list=[]
    say_dance=False
    for move in range(dance_length):
        generateMove=randint(-2,1)
        move_list.append(generateMove)
        display_list.append(generateMove)
    
    show_countdown=True
    print(move_list)
    countdown()
    return

def update():
    global game_over, current_move, moves_complete,level
    if not game_over:
        if moves_complete:
            level+=1
            generate_moves()
            moves_complete=False
            current_move=0
        


#music.play("vanishing-horizon")
generate_moves()
pgzrun.go()
