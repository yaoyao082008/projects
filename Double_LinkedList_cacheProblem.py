
class Node:
    def __init__(self,data):
        self.data=data
        self.next=self
        self.prev=self
class DoubleLinkedListCycle:
    def __init__(self):
        self.root=None
        self.length=0
    
    def print(self):
        if self.length==0:
            raise Exception('list empty')
        itr=self.root
        while itr!=self.root.prev:
            print(str(itr.data)+" --> ",end='')
            itr=itr.next
        print(str(itr.data)+" --> ")

    def insert_end(self,data):
        self.length+=1
        node=Node(data)
        if self.root is None:
            self.root=node
            return self.root

        temp=self.root.prev
        itr=self.root.prev
        itr.next=node
        self.root.prev=itr.next
        self.root.prev.next=self.root
        self.root.prev.prev=temp
        return self.root.prev

    def delete(self,node=None):
        self.length-=1
        if node==None or node==self.root:
            temp=self.root.prev
            self.root=self.root.next
            self.root.prev=temp
            temp.next=self.root
            return 
        node=node.prev
        node.next=node.next.next
        node=node.next
        node.prev=node.prev.prev

    def is_empty(self):
        if self.length==0:
            return True
        return False


