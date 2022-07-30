from linkedlist import *
from BinaryHeapForLL import *
from random import randint

def create_lines(lines):
    total_length=0
    for i in range(int(lines)):
        name='line'+str(i)
        num_vals=input('how many values do you want? ')
        globals()[name]=LinkedList()
        temp=[]
        for j in range(int(num_vals)):
            temp.append(randint(0,100))
            temp.sort()
        for k in range(int(num_vals)):
            globals()[name].insert_end(temp[k])
        total_length+=int(num_vals)
    return total_length

def merge(numOfLines,total_length):
    merged_line=[]
    min_itr= BinaryMinHeapN()
    for i in range(numOfLines):
        name='line'+str(i)
        min_itr.insert(globals()[name].root)
    
    for i in range(total_length):
        merged_line.append(min_itr.storage[0].data)
        if min_itr.storage[0].next:
            min_itr.storage[0]=min_itr.storage[0].next
            min_itr.heapify_down()
        else:
            min_itr.delete()
    print(merged_line)



num=input('how many lines : ')
l=create_lines(num)
merge(int(num),l)