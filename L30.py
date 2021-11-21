from  random import randint
from itertools import cycle
from tkinter import Canvas,Tk,messagebox,font
canvas_width=800
canvas_height=400
root=Tk()
c=Canvas(root,width=canvas_width,height=canvas_height,background='blue')
c.create_rectangle(-5,canvas_height-150,canvas_width+10,\
    canvas_height+10,fill='green',width=0)
c.create_oval(-80,-80,120,120,fill='orange',width=0)
c.pack()

color_cycle=cycle(["light blue",'aqua','purple','gold','green','royal blue','red'])
egg_width=45
egg_height=55
egg_score=10
egg_speed=700
egg_interval=4000
difficulty_factor=0.95

catcher_color="blue"
catcher_width=100
catcher_height=100
catcher_start_x=canvas_width/2-catcher_width/2 
catcher_start_y=canvas_height-catcher_height-20
catcher_start_x2=canvas_width/2+catcher_width/2
catcher_start_y2=catcher_start_y+catcher_height
catcher=c.create_arc(catcher_start_x,catcher_start_y,catcher_start_x2,catcher_start_y2,start=180,extent=180,style='arc',outline=catcher_color,width=3)
game_over=False
game_font=font.nametofont("TkFixedFont")
game_font.config(size=18)
#end_screen=font.nametofont("TkFixedFont")
#end_screen.config(size=50)


score=0
lives_remaining=3
display_score=c.create_text(65,50,text="score= %s"%score,fill='black',font=game_font)
display_lives=c.create_text(720,50,text="Lives= "+str(lives_remaining),fill='black',font=game_font)

eggs=[]
def create_egg():
    if not game_over:
        x=randint(0,750)
        y=40
        egg=c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
        eggs.append(egg)
        root.after(egg_interval,create_egg)
def move_egg():
    if not game_over:
        for egg in eggs:
            (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
            c.move(egg,0,10)
            if egg_y2>canvas_height:
                egg_dropped(egg)
        root.after(egg_speed,move_egg)       
def catch_egg():
    global score,lives_remaining,egg_speed
    (catcher_x,catcher_y,catcher_x2,catcher_y2)=c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2)=c.coords(egg)
        if catcher_x<egg_x and egg_x2<catcher_x2 and (catcher_y2-egg_y2)<40:
            if egg_speed>=300:
                egg_speed-=50
            eggs.remove(egg)
            c.delete(egg)
            score+=1
            c.itemconfigure(display_score,text="score= %s"%score)
    root.after(egg_speed,catch_egg)

def egg_dropped(egg):
    global game_over,lives_remaining
    eggs.remove(egg)
    c.delete(egg)
    lives_remaining-=1
    c.itemconfigure(display_lives,text="Lives= "+str(lives_remaining))
    if lives_remaining<=0:
        game_over=True
        c.create_rectangle(0,0,canvas_width,canvas_height,fill="green")
        c.create_text(canvas_width/2,canvas_height/2,text="GAME OVER",fill='black',font="Arial 50")
        
        
    
def move_right(event):
    x1=c.coords(catcher)
    if x1[2] <canvas_width:
        c.move(catcher,13,0)
def move_left(event):
    x1=c.coords(catcher)
    if x1[0]>0:
        c.move(catcher,-13,0)

root.bind("<Right>",move_right)
root.bind("<Left>",move_left)
root.after(1000,create_egg)
root.after(1000,move_egg)
root.after(1000,catch_egg)
