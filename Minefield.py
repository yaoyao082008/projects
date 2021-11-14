from random import randint
C=4
R=3
def createminefield(C,R,M):
    global minefield
    minefield=[[0 for i in range(C)]for i in range(R)]
    while M>0:
        x=randint(0,R-1)
        y=randint(0,C-1)
        if minefield[x][y]!=1:
            M-=1
        minefield[x][y]=1

createminefield(C,R,5)
print(minefield)