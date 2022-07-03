def binary_search(arr,start,end,target):
    mid=(start+end)//2

    if end-start<1:
        return start
    elif arr[mid]<=target:
        return binary_search(arr,mid+1,end,target)
    elif arr[mid]>target:
        return binary_search(arr,start,mid-1,target)

target=1
arr=[1,2,3,4,5,6,7,8,9,10]
k=binary_search(arr,0,len(arr)-1,target)
if arr[k]!=target:
    print(-1)
else:
    print(k)
