

def median(arr,start,end):
    mid=partitian(arr,start,end-1,end)

    if mid==len(arr)//2:
        return arr[mid]
    elif mid<len(arr)//2:
        start=mid+1
    else:
        end=mid-1
    return median(arr,start,end)




def partitian(arr,start,end,END):
    
    partPoint=arr[END]

    while arr[start]<partPoint or arr[end]>partPoint:
        if arr[start]<partPoint:
            start+=1
        if arr[end]>partPoint:
            end-=1


    if start>end:
        arr[start],arr[END]=arr[END],arr[start]
        return start

    arr[start],arr[end]=arr[end],arr[start]

    return partitian(arr,start+1,end-1,END)


arr=[26,90,12,89,100]
print(median(arr,0,len(arr)-1))
print(arr)

