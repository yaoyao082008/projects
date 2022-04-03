Array=[1,6]
target=2
starting=0
ending=len(Array)-1
while ending-starting>=1:
    splittingPoint=(starting+ending)//2
    if Array[splittingPoint]<target:
        starting=splittingPoint+1
    else:
        ending=splittingPoint
if Array[starting]==target:
    print(starting)
else:
    print(-1)