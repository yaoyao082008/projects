from linkedlist import *
ll=LinkedList()
for i in range(10):
    ll.insert_end(i+1)

def reverse(ll):
    itr=ll.root
    prev=None
    temp=ll.root
    while itr:
        temp=itr.next
        itr.next=prev
        prev=itr
        itr=temp
    ll.root=prev
    return ll


def reverse_simple(ll):
    itr=ll.root
    newroot=None
    while itr:
        temp=newroot
        newroot=itr
        itr=itr.next
        newroot.next=temp
    ll.root=newroot
    return ll


def cycle(ll):
    itr=ll.root
    while itr.next:
        itr=itr.next
    itr.next=ll.root
    return ll


def reverse_recursion(ll):
    
    reverse_recursion(ll)
ll.print()
reverse_recursion(ll)
ll.print()
