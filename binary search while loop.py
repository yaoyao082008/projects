Array=[1,6,9,11,15]
target=11
starting=0
ending=len(Array)-1
while ending-starting>=1:
    splittingPoint=(starting+ending)//2
    if Array[splittingPoint]<target:
        starting=splittingPoint+1
    elif Array[splittingPoint]>=target:
        ending=splittingPoint
if Array[starting]==target:
    print(starting)
else:
    print(-1)