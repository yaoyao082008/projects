
Array=[5,8,10,15]
LengthOfArray=len(Array)-1
target=11
run=True
totalMissingNumbers= Array[LengthOfArray]-Array[0]-LengthOfArray
if target>Array[0]:
    target=target-Array[0]+1
elif target<Array[0]:
    print(target)
    run=False

if target>totalMissingNumbers:
    print(Array[LengthOfArray]+(target-totalMissingNumbers))
elif run==True:
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


        
