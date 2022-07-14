

def sort (low,high,arr):
    if low<0:
        low=-low
    key=[0 for i in range(low+high+1)]
    for i in range(len(arr)):
        key[arr[i]+low]+=1
    start=0
    for i in range(len(key)):
        for j in range(key[i]):
            arr[start]=i-low
            start+=1
    return arr

arr=[6,6,4,3,2,1,0,0,2]
arr=sort(0,6,arr)
print(arr)