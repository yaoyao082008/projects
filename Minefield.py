from random import randint
from tkinter import Tk, Button, DISABLED
buttons={}
root=Tk()
minestoclear=10

class neighbourhood:
    def __init__(self,deltaI,deltaJ):
        self.deltaI=deltaI
        self.deltaJ=deltaJ
#list 
neighbours=[]
neighbours.append(neighbourhood(-1,-1))
neighbours.append(neighbourhood(-1,0))
neighbours.append(neighbourhood(-1,1))
neighbours.append(neighbourhood(0,-1))
neighbours.append(neighbourhood(0,1))
neighbours.append(neighbourhood(1,-1))
neighbours.append(neighbourhood(1,0))
neighbours.append(neighbourhood(1,1))
def createminefield(C,R,M):
    minefield=[[-2 for i in range(C)]for i in range(R)]
    while M>0:
        x=randint(0,R-1)
        y=randint(0,C-1)
        if minefield[x][y]!=-1:
            M-=1
        minefield[x][y]=-1
    return minefield
def get_neibourhood(matrix,R,C):
    minesnearby=0
    for x in range(R):
        for y in range(C):
            minesnearby=0
            for obj in neighbours:
                posX= obj.deltaI
                posY=obj.deltaJ
                if x+posX>=0 and x+posX<R and y+posY>=0 and y+posY<C and matrix[x][y]!=-1:
                    if matrix[x+posX][y+posY]==-1:
                        minesnearby+=1
                        matrix[x][y]=minesnearby

R=9
C=9
matrix=createminefield(C,R,10 )
newminefield=get_neibourhood(matrix,R,C)

def show_symbol(x,y):
    buttons[x,y]['text']=matrix[x][y]
    show_neighbours(x,y)
    gameover(x,y)
    print("y: %s x: %d" %(y,x))
def show_neighbours(x,y):
    if matrix[x][y]==0:
        return 
    if matrix[x][y]==-2:
        matrix[x][y]=0
        for obj in neighbours:
            posX= obj.deltaI
            posY=obj.deltaJ
            if x+posX>=0 and x+posX<R and y+posY>=0 and y+posY<C:
                buttons[x+posX,y+posY]['text']=matrix[x+posX][y+posY]
                if matrix[x+posX][y+posY]==-2:       
                    show_neighbours(x+posX,y+posY)

def gameover(x,y):
    if matrix[x][y]==-1:
        pass
def Flag(event):
    global minestoclear
    minestoclear-=1
    buttons[event.x_root,event.y_root]['text']=('M')
def win_game():
    pass
for x in range(R):
    for y in range(C):
        button=Button(root,command=lambda  x=x, y=y:show_symbol(x,y), width=3,height=2,bg="light green")
        button.grid(column=x,row=y)
        buttons[x,y]=button
        buttons[x,y].bind("<Button-3>",Flag)
root.mainloop()
