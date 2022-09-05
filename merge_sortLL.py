from linkedlist import *


def Merge_Sort(result):
    if result.next is None:
        return
    left=result
    itr=result
    itr2=result.next
    while itr2 and itr2.next:
        itr=itr.next
        itr2=itr2.next
        if itr2:
            itr2=itr2.next
    right=itr.next
    itr.next=None
    Merge_Sort(left)
    Merge_Sort(right)
    if left.data<right.data:
        t=left.next
        result=left
        left.next=None
        left=t
    else:
        t=right.next
        result=right
        right.next=None
        right=t
    itr1=result
    while left or right:
        if not left:
            tempr=right.next
            itr1.next=right
            right.next=None
            right=tempr
        elif not right:
            templ=left.next
            itr1.next=left
            left.next=None
            left=templ
        elif left.data<right.data:
            templ=left.next
            itr1.next=left
            left.next=None
            left=templ
        else:
            tempr=right.next
            itr1.next=right
            right.next=None
            right=tempr
        itr1=itr1.next




    
            





arr=LinkedList()
arr.insert_end(3)
arr.insert_end(5)
arr.insert_end(2)
arr.insert_end(4)
arr.insert_end(12)
arr.insert_end(14)
arr.insert_end(13)
arr.insert_end(22)
#arr.insert_end(7)

Merge_Sort(arr.root)
arr.print()
   