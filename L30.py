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
egg_speed=500
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

game_font=font.nametofont("TkFixedFont")
game_font.config(size=18)


score=0
lives_remaining=3
c.create_text(65,50,text="score= %s"%score,fill='black',font=game_font)
c.create_text(720,50,text="Lives= "+str(lives_remaining),fill='black',font=game_font)

eggs=[]
def create_egg():
    x=randint(0,750)
    y=40
    egg=c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(egg)
    root.after(egg_interval,create_egg)
    
def move_right(event):
    x1=c.coords(catcher)
    if x1[2] <width:
        c.move(catcher,6,0)
def move_left(event):
    x1=c.coords(catcher)
    if x1[0]>0:
        c.move(catcher,-6,0)

root.bind("<Right>",move_right)
root.bind("<Left>",move_left)
root.after(1000,create_egg)
