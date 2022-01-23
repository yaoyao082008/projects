from tracemalloc import start
Array=[1,3,5,7,11,18,20]
LengthOfArray=len(Array)-1
totalMissingNumbers= Array[LengthOfArray]-Array[0]-LengthOfArray
target=7
if target>totalMissingNumbers:
    print(Array[len(Array)-1]+(target-totalMissingNumbers))
else:
    MissingNumbersHalf=0
    NthmissingNumber=0
    starting=0
    ending=len(Array)-1
    while True:
        splittingPoint=(starting+ending)//2
        MissingNumbersHalf=Array[splittingPoint]-Array[starting]-(splittingPoint-starting)
        if MissingNumbersHalf<=target:
            target=target-MissingNumbersHalf
            if Array[splittingPoint+1]-Array[splittingPoint]>target:
                print(Array[splittingPoint]+target)
                break
            starting=splittingPoint
        
