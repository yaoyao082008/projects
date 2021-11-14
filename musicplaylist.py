import random 
array1 = [1,2,3,4,5]
def song( whichTime,start):
    if whichTime<3:
        k=random.randint(whichTime,len(array1)-1)
        array1[k],array1[whichTime]=array1[whichTime],array1[k]
        return whichTime
    k=random.randint(3,len(array1)-1) 
    """chooses between the 3rd song and the last"""
    array1[k],array1[start]=array1[start],array1[k] 
    """swaps the values so that it won't repeat"""
    return start    
    """returns the value of start """


time_to_play=20
j=0
for i in range(time_to_play):
    if j==3:
        j=0
    """helps keep track of the previous 3 songs"""
    k=song(i,j)
    j+=1
    print(array1[k],i) 