
def Merge_Sort(arr):
    if len(arr)<=1:
        return
    left_arr=arr[:len(arr)//2]
    right_arr=arr[len(arr)//2:]
    Merge_Sort(left_arr)
    Merge_Sort(right_arr)
    i=0
    j=0
    k=0
    while i<len(left_arr) or j<len(right_arr):
        if i>=len(left_arr):
            arr[k]=right_arr[j]
            j+=1
        elif j>=len(right_arr):
            arr[k]=left_arr[i]
            i+=1
        elif left_arr[i]>right_arr[j]:
            arr[k]=right_arr[j]
            j+=1
        else:
            arr[k]=left_arr[i]
            i+=1
        k+=1
        






arr=[10,7,8,15,12,14,13,22,7]
Merge_Sort(arr)
print(arr)