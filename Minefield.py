from random import randint

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
    minefield=[[0 for i in range(C)]for i in range(R)]
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


R=6
C=6
matrix=createminefield(C,R,13)
newminefield=get_neibourhood(matrix,R,C)
for i in range(R):
    for j in range(C):
        print(matrix[i][j],end=" ")
    print()
