

def median(arr,start,end,mid_point,layer):
    mid=partitian(arr,start,end-1,end,layer)

    if mid==mid_point:
        return mid
    elif mid<mid_point:
        start=mid+1
    else:
        end=mid-1
    return median(arr,start,end,mid_point,layer)




def partitian(arr,start,end,END,layer):
    
    partPoint=arr[END][layer]

    while arr[start][layer]<partPoint or arr[end][layer]>partPoint:
        if arr[start][layer]<partPoint:
            start+=1
        if arr[end][layer]>partPoint:
            end-=1

    if start>end:
        arr[start],arr[END]=arr[END],arr[start]
        return start

    arr[start],arr[end]=arr[end],arr[start]

    return partitian(arr,start+1,end-1,END,layer)


