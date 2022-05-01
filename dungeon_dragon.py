import pgzrun
import math
import random
import time

WIDTH=800
HEIGHT=600
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
FONT_COLOR=(0,0,0)
EGG_TARGET=20
HERO_START=(100,300)
HERO2_START=(300,300)
ATTACK_DISTANCE=200
DRAGON_WAKE_TIME=2
EGG_HIDE_TIME=2
MOVE_DISTANCE=5


lives=3
eggs_collected=0
game_over=False
game_complete=False
reset_required=False

easy_lair={
    "dragon":Actor("dragon-asleep", pos=(600,100)),
    "eggs":Actor("one-egg", pos=(400,100)),
    "egg_count":1,
    "egg_hidden":False,
    "egg_hide_counter":0,
    "sleep_length":12,
    "sleep_counter":0,
    "wake_counter":0,
    "fire":3
}


medium_lair={
    "dragon":Actor("dragon-asleep", pos=(600,266)),
    "eggs":Actor("two-eggs", pos=(400,266)),
    "egg_count":2,
    "egg_hidden":False,
    "egg_hide_counter":0,
    "sleep_length":7,
    "sleep_counter":0,
    "wake_counter":0,
    "fire":5
}


hard_lair={
    "dragon":Actor("dragon-asleep", pos=(600,432)),
    "eggs":Actor("three-eggs", pos=(400,432)),
    "egg_count":3,
    "egg_hidden":False,
    "egg_hide_counter":0,
    "sleep_length":4,
    "sleep_counter":0,
    "wake_counter":0,
    "fire":7
}
hero=Actor('hero', pos=HERO_START)

dragons=[hard_lair,medium_lair,easy_lair]

def draw():
    global dragons,eggs_collected,lives
    if game_over:
        screen.blit('dungeon',(0,0))
    else:
        screen.blit('dungeon',(0,0))
        for dragon in dragons:
            dragon['dragon'].draw()
            if not dragon["egg_hidden"]:
                dragon['eggs'].draw()
    hero.draw()
    draw_counter(eggs_collected,lives)
def draw_counter(eggs_collect,lives):
    screen.blit("egg-count", (0, HEIGHT-30))
    screen.draw.text(str(eggs_collected),\
         fontsize=40,pos=(30,HEIGHT-30),color=FONT_COLOR)
    screen.draw.text(str(lives),fontsize=40,pos=(90,HEIGHT-30),color=FONT_COLOR)
    

def update():
    global game_over,dragons,eggs_collected,lives
    if lives==0:
        game_over=True
    if not game_over:
        if keyboard.left:
            hero.x-=5
            if hero.x <0:
                hero.x=WIDTH-50
        elif keyboard.right:
            hero.x+=5
            if hero.x>WIDTH:
                hero.x=50
        elif keyboard.up:
            hero.y-=5
            if hero.y<50:
                hero.y= HEIGHT-150
        elif keyboard.down:
            hero.y+=5
            if hero.y>HEIGHT-100:
                hero.y=150
        for dragon in dragons:
            
            if hero.colliderect(dragon['eggs']) and dragon['dragon'].image=="dragon-asleep":
                if not dragon["egg_hidden"]:
                    eggs_collected+=dragon['egg_count']
                    dragon['egg_hidden']=True
                    print(dragon['egg_hidden'])
                    #clock.schedule(reappear,EGG_HIDE_TIME)
            elif hero.colliderect(dragon['eggs']) and dragon['dragon'].image=="dragon-awake":
                lives-=1
                hero.pos=(CENTER_X/2,CENTER_Y/2)
def reappear():
    global dragons,game_over
    for dragon in dragons:
        if dragon['egg_hidden']==True:
            if dragon['egg_hide_counter']>=EGG_HIDE_TIME:
                dragon['egg_hidden']=False
                dragon['egg_hide_counter']=0
            else:
                dragon['egg_hide_counter']+=1
def shoot_fire():
    global game_over,dragons
    if game_over:
        return
    for dragon in dragons:
        
        if dragon["sleep_counter"]>dragon["sleep_length"]:
            
            dragon['dragon'].image='dragon-awake'
            dragon["sleep_counter"]=0
        else:
            dragon['sleep_counter']+=1  

def asleep():
    global game_over,dragons
    if game_over:
        return
    for dragon in dragons:
        
        if dragon["wake_counter"]>=dragon["fire"]:
            
            dragon['dragon'].image='dragon-asleep'
            dragon["wake_counter"]=0
        else:
            dragon['wake_counter']+=1  
clock.schedule_interval(shoot_fire,1)
clock.schedule_interval(asleep,1)
clock.schedule_interval(reappear,1)
pgzrun.go()


























