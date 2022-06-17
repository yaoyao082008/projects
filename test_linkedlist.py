
class Node:
    def __init__(self, data , next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.root=None
    def insert_beggining(self,data):
        node=Node(data,self.root)
        self.root=node
    def print(self):
        if self.root is None:
            print('list empty')
            return
        itr=self.root
        linkListstr=''
        while itr:
            linkListstr+= str(itr.data)+" --> "
            itr= itr.next
        print(linkListstr)

    def insert_end(self,data):
        node=Node(data,None)
        if self.root is None:
            self.root=node
            return
        itr=self.root
        while itr.next:
            itr=itr.next
        itr.next=node

    def length(self):
        itr=self.root
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def delete(self,index):
        if index<0 or index>= self.length():
            print('not valid')
            return
        if index==0:
            self.root=self.root.next
            return
        count=0
        itr=self.root
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                return
            itr=itr.next
            count+=1
    
    def insert_at(self,index,data):
        if index<0 or index>= self.length():
            print('not valid')
            return
        itr=self.root
        count=0
        while itr:
            if count==index:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def remove_value(self,data):
        itr=self.root
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next
        print('no such value')
        return 

    def insert_by_value(self,value,data):
        itr=self.root
        while itr:
            if itr.data==value:
                node=Node(data,itr.next)
                itr.next=node
                return
            itr=itr.next
        print('no value found')
        return

    def reverse(self):
        itr=self.root
        prev=None
        temp=self.root
        while itr:
            temp=itr.next
            itr.next=prev
            prev=itr
            itr=temp
        self.root=prev
    def reverse_ez(self):
        itr=self.root
        newroot=None
        while itr:
            temp=newroot
            newroot=itr
            itr=itr.next
            newroot.next=temp
        
        self.root=newroot

ll=LinkedList()
for i in range(10):
    ll.insert_end(i)
#ll.reverse()
ll.print()
ll.reverse_ez()
ll.print()
    


