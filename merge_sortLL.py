from turtle import right
from linkedlist import *

def Merge_Sort(arr):
    if not arr:
        return

    Merge_Sort(left)
    Merge_Sort(right_s)
    print()



arr=LinkedList()
arr.insert_end(10)
arr.insert_end(9)
arr.insert_end(12)
arr.insert_end(14)
arr.insert_end(13)
arr.insert_end(12)
arr.insert_end(0)

Merge_Sort(arr.root)
arr.print()