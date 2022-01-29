Array=[1,5]
LengthOfArray=len(Array)-1
target=6
if Array[0]!=1:
    Array.insert(0,1)
totalMissingNumbers= Array[LengthOfArray]-Array[0]-LengthOfArray
MissingNumbersHalf=0
NthmissingNumber=0
starting=0
ending=len(Array)-1
while True:
    splittingPoint=(starting+ending)//2
    MissingNumbersHalf=Array[splittingPoint]-Array[starting]-(splittingPoint-starting)
    if MissingNumbersHalf<target:
        target=target-MissingNumbersHalf
        if Array[splittingPoint+1]-Array[splittingPoint]>target:
            print(Array[splittingPoint]+target)
            break
        starting=splittingPoint
    elif MissingNumbersHalf>=target:
        ending=splittingPoint
