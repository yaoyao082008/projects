
class Node:
    def __init__(self,data):
        self.data=data
        self.next=self
        self.prev=self
class DoubleLinkedListCycle:
    def __init__(self):
        self.root=None
        self.length=0
    def insert_at(self,data,pos,cursor):
        node=Node(data)
        if pos==None:
            self.root=node
            self.length+=1
            return
        temp=pos
        temp1=pos.next
        pos.next=node
        node.prev=temp
        node.next=temp1
        self.length+=1
        pos=pos.next
        if cursor==self.length-2:
            pos.next=self.root
            self.root.prev=pos
    def print_ll(self):
        if self.length==0:
            raise Exception('list empty')
        itr=self.root
        while itr!=self.root.prev:
            print(str(itr.data)+" --> ",end='')
            itr=itr.next
        print(str(itr.data)+" --> ",end='')

    def delete_at(self,pos,cursor):
        if pos==None:
            raise Exception ('not valid')
        pos.next=pos.next.next
        pos=pos.next
        pos.prev=pos.prev.prev
        pos=pos.prev
        self.length-=1



