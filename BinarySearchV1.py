Array=[0,3,4,5,9,10]
kthMissingNumber=6
target=7
def search(starting,ending):
    middle=(starting+ending)//2
    if ending-starting<=0:
        return starting
    elif Array[middle]<target:
        return search(middle+1,ending)
    elif Array[middle]>=target:
        return search(starting,middle)

k=search(0,len(Array)-1)
if Array[k]==target:
    print(k)
else:
    print(-1)


