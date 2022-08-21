from linkedlist import *

def Merge_Sort(arr):
    if arr.length<=1:
        return
    left_arr,mid=arr.slice_mid_left()
    right_arr=arr.slice_mid_right(mid)
    
    Merge_Sort(left_arr)
    Merge_Sort(right_arr)

    i=left_arr.root
    j=right_arr.root
    k=arr.root
    while i or j:
        if not i :
            k.data=j.data
            j=j.next
        elif not j:
            k.data=i.data
            i=i.next
        elif i.data>j.data:
            k.data=j.data
            j=j.next
        else:
            k.data=i.data
            i=i.next
        k=k.next


arr=LinkedList()
arr.insert_end(10)
arr.insert_end(9)
arr.insert_end(12)
arr.insert_end(14)
arr.insert_end(13)
arr.insert_end(12)
arr.insert_end(0)

Merge_Sort(arr)
arr.print()