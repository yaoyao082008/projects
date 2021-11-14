import random
array1=(2,5,6,8,1,3)
def picksong(whichtime):
    if whichtime ==0:
        start=0
        k=random.randint(start,len(array1)-1)
        array1[k],array1[start]=array1[start],array1[k]
        return start