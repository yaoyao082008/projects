import pgzrun
import random

apple=Actor("apple")
#beijingcorn=Actor("beijingcorn.jpg")
def placeApple():
    apple.x=random.randint(0,500)
    apple.y=random.randint(0,300)
def draw():
    #screen.draw.text("topright",topright=(random.randint(0,500),random.randint(0,500)))
    #screen.draw.text("topleft",topleft=(random.randint(0,500),random.randint(0,500)))
    #screen.draw.text("center",center=(random.randint(0,500),random.randint(0,500)))
    #apple.draw()
    screen.clear()   
    apple.draw()
    #beijingcorn.draw()
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        placeApple()
    else:
        screen.draw.text("hello",topleft=(300,300))
pgzrun.go()
