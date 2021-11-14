from random import randint

def createminefield(C,R,M):
    minefield=[[0 for i in range(C)]for i in range(R)]
    while M>0:
        x=randint(0,R-1)
        y=randint(0,C-1)
        if minefield[x][y]!=1:
            M-=1
        minefield[x][y]=1
    return minefield

R=4
C=3
matrix=createminefield(C,R,5)
print(matrix)