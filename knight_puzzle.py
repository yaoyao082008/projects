import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from random import randint

class knight_puzzle:
    

    def __init__(self):
        #basics
        self.board=tk.Tk()
        self.board.title("Move the knight to the square in the least amount of moves")
        self.coor=[]
        self.w=10
        self.h=5
        self.cur_coor=[0,0]
        self.start_coor=[0,0]
        self.target_coor=[1,1]

        #win_cons
        self.min_moves=0
        self.cur_moves=0
        self.knight_moves=[(-2,1),(2,-1),(-2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
        self.won=False
        

        image = Image.open("knight.png")
        k = image.resize((70,70))
        self.knight= ImageTk.PhotoImage(k)

        #board
        for x in range(8):
            row=[]
            for y in range(8):
                frame = tk.Frame(master=self.board,borderwidth=1)
                frame.grid(row=x, column=y)  # line 13
                if x%2==0 and y%2==0 or x%2!=0 and y%2!=0:
                    label = tk.Button(frame,bg='white',width=self.w,\
                        height=self.h,command=lambda coor=(x,y):self.move(coor))
                else:
                    label = tk.Button(frame,bg='black',width=self.w,\
                        height=self.h,command=lambda coor=(x,y):self.move(coor))
                row.append(label)
                label.pack()
            self.coor.append(row)
        self.start_game()
        
    def move(self,coor):
        x,y=coor

        if self.coor[x][y]['width']==0:
            return
        else:
            # check for legal move
            x1,y1=self.cur_coor
            if abs(x1-x)==2 and abs(y1-y)==1 or abs(x1-x)==1 and abs(y1-y)==2:
                if x1%2==0 and y1%2==0 or x1%2!=0 and y1%2!=0:
                    self.coor[x1][y1].config(width=self.w,height=self.h,bg='white',image='')
                else:
                    self.coor[x1][y1].config(width=self.w,height=self.h,bg='black',image='')

                self.coor[x][y].config(width=0,height=0,image=self.knight)
                self.cur_coor=[x,y]

            # check game_over
            if self.game_over():
                messagebox.showinfo('goodjob','congratulation you did it!')
                self.board.destroy()
            return

    def start_game(self):
        # x,y=[randint(0,7),randint(0,7)]
        # x1,y1=[randint(0,7),randint(0,7)]
        x,y=[3,3]
        x1,y1=[4,4]

        while x==x1 and y==y1:
            x,y=[randint(0,7),randint(0,7)]
            x1,y1=[randint(0,7),randint(0,7)]
            
        self.start_coor=[x,y]
        self.cur_coor=[x,y]
        self.target_coor=[x1,y1]
        self.coor[x1][y1].config(bg='red')
        self.coor[x][y].config(width=0,height=0,image=self.knight)

        # min=self.calculate_best_moves(self.cur_coor,0,set())
        # self.min_moves=min
        # print(self.min_moves)

    def game_over(self):
        return self.cur_coor==self.target_coor

    # def calculate_best_moves(self,coor,moves,visited):
    #     if coor==self.target_coor:
    #         return moves

    #     for move in self.knight_moves:
    #         x,y=move
    #         x1,y1=coor
    #         visited.add((x1,y1))

    #         if 0<=x1+x<=7 and 0<=y1+y<=7 and (x1+x,y1+y) not in visited:
    #             val=self.calculate_best_moves([x1+x,y1+y],moves+1,visited)
    #             self.min_moves.append(val)

        
    #     return min(self.min_moves)

        
          
        
        

game=knight_puzzle()
game.board.mainloop()