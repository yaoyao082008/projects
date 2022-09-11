from linkedlist import *


def Merge_Sort(ll):
    if ll.next is None:
        return ll

    right=ll
    left=ll
    fast=ll

# divdes linkedlist in half
    while fast:
        prev=right
        right=right.next
        fast=fast.next
        if fast:
            fast=fast.next

# breaks the 2 halves
    prev.next=None

    left=Merge_Sort(left)
    right=Merge_Sort(right)

# return merge sorted result
    return sorted_merge(left,right,ll)



                
def sorted_merge(left,right,result):
# set root
    if left.data<right.data:
        result=left
        left=left.next
    else:
        result=right
        right=right.next

    itr=result

#merge
    while left or right:
        if not left:
            itr.next=right
            right=right.next
        elif not right:
            itr.next=left
            left=left.next
        elif right.data<left.data:
            itr.next=right
            right=right.next
        else:
            itr.next=left
            left=left.next
        itr=itr.next

    return result


arr=LinkedList()
arr.insert_end(5)
arr.insert_end(3)
arr.insert_end(4)
arr.insert_end(2)
arr.insert_end(12)
arr.insert_end(14)
arr.insert_end(13)
arr.insert_end(22)
arr.insert_end(7)

root=Merge_Sort(arr.root)
arr.root=root
arr.print()
   