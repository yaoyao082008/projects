from random import randint
from tkinter import Tk, Frame, Label
from tkinter import*
from PIL import Image , ImageTk
from tkinter import messagebox
labels={}
buttons={}
winCon=0
minestoclear=10
# from tkinter import *
# from tkinter.ttk import *

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
def show_neighbours(x,y):
    if matrix[x][y]=="":
        return 
    if matrix[x][y]==-2:
        matrix[x][y]=""
        labels[x,y].configure(text=matrix[x][y])
        for obj in neighbours:
            posX= obj.deltaI
            posY=obj.deltaJ
            if x+posX>=0 and x+posX<R and y+posY>=0 and y+posY<C:
                labels[x+posX,y+posY].configure(text=matrix[x+posX][y+posY])
                buttons[x+posX,y+posY].config(background='light green',relief=SUNKEN)
                if matrix[x+posX][y+posY]==-2:       
                    show_neighbours(x+posX,y+posY)
    


R=9
C=9
matrix=createminefield(C,R,10)
newminefield=get_neibourhood(matrix,R,C)




def left(event):
    master.title('clicked left')
    x = event.x_root - master.winfo_rootx()
    y = event.y_root - master.winfo_rooty()
    z = master.grid_location(x,y)
    buttonx=z[0]
    buttony=z[1]
    labels[buttonx,buttony]['text']=matrix[buttonx][buttony]
    buttons[buttonx,buttony].config(relief=SUNKEN)
    if matrix[buttonx][buttony]==-1:
        messagebox.showinfo('GAMEOVER','Sadly you clicked on a mine and died')
        master.destroy()
    if matrix[buttonx][buttony]==-2:
        show_neighbours(buttonx,buttony)
    #button.config(fg='blue')
    
def right(event):
    global winCon,minestoclear
    master.title('clicked right')
    x = event.x_root - master.winfo_rootx()
    y = event.y_root - master.winfo_rooty()
 
    # Here grid_location() method is used to
    # retrieve the relative position on the
    # parent widget
    z = master.grid_location(x,y)
    buttonx=z[0]
    buttony=z[1]
    #if minestoclear>0:
    if labels[buttonx,buttony]['width']==0:
        labels[buttonx,buttony].config(width=4,height=2,image='')
    else:
        labels[buttonx,buttony].config(width=0,height=0,image=flag)
        #if matrix[buttonx][buttony]==-1:
        #    winCon+=1
        #if winCon==10:
        #    messagebox.showinfo('game won','congrats you won minesweeper easy mode')
        #    master.destroy()
    #if labels[buttonx,buttony]['width']==0:
    #    labels[buttonx,buttony].config(width=4,height=2,image='')

master = Tk()
#flag= PhotoImage(file="C:\\Users\\Quanren.Xiong\\Downloads\\flag_icon.png")
image = Image.open("C:\\Users\\Quanren.Xiong\\Downloads\\flag_icon.png")
flag1 = image.resize((30,30))
flag= ImageTk.PhotoImage(flag1)
#f = Frame(master, background="white")
#f.pack()

for x in range(R):
    for y in range(C):
        #button=Button(root, command=lambda  x=x, y=y:show_symbol(x,y), width=4,height=4)
        button = Frame(master, width=20, height=20,bg='green',borderwidth=1)
        button.grid(column=x,row=y)
        buttons[x,y]=button
        #label = Label(button, text=f"Row {x}\nColumn {y}")
        label = Label(button,width=4,height=2)
        label.bind('<Button-3>', right)
        label.bind('<Button-1>',left)
        label.pack()
        #button.pack()
        labels[x,y]=label
        # buttons[x,y].bind('<Button-1>', left)   # bind left mouse click
        #buttons[x,y].bind('<Button-3>', right)  # bind right mouse click
master.mainloop()
