
Array=[5,6]
LengthOfArray=len(Array)-1
target=5
before=Array[0]-1
totalMissingNumbers= Array[LengthOfArray]-Array[0]-LengthOfArray+before
MissingNumbersHalf=0
starting=0
ending=len(Array)-1
splittingPoint=0
if target>totalMissingNumbers:
    print(Array[LengthOfArray]+(target-totalMissingNumbers))
elif target<Array[0]:
    print(target)
else:
    target=target-Array[0]+1
    while Array[splittingPoint+1]-Array[splittingPoint]<=target:
        splittingPoint=(starting+ending)//2
        MissingNumbersHalf=Array[splittingPoint]-Array[starting]-(splittingPoint-starting)
        if MissingNumbersHalf<target:
            target=target-MissingNumbersHalf
            starting=splittingPoint
        elif MissingNumbersHalf>=target:
            ending=splittingPoint
    print(Array[splittingPoint]+target)


        
