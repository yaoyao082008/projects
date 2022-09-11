from linkedlist import *
ll=LinkedList()
for i in range(10):
    ll.insert_end(i+1)

def reverse(ll):
    itr=ll.root
    prev=None
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

#[1-->2-->3-->4-->5-->6-->7-->8-->9-->10-->None]
#[None<--1<--2<--3<--4<--5<--6<--7<--8<--9<--10]


def reverse_recursion(itr):
    if itr==None or itr.next==None: 
        return (itr, itr)
    (newroot, tail)=reverse_recursion(itr.next)
    tail.next = itr
    itr.next=None
    return (newroot, itr)

root,itr=reverse_recursion(ll.root)
ll.root=root
ll.print()







"""if left.data<right.data:
        left=left.next
    else:
        t=right.next
        result=right
        right.next=None
        right=t
    itr=result

    while left or right:
        if not left:
            tempr=right.next
            itr.next=right
            right.next=None
            right=tempr
        elif not right:
            templ=left.next
            itr.next=left
            left.next=None
            left=templ
        elif left.data<right.data:
            templ=left.next
            itr.next=left
            left.next=None
            left=templ
        else:
            tempr=right.next
            itr.next=right
            right.next=None
            right=tempr
        itr=itr.next

    arr.root=result

    return result"""