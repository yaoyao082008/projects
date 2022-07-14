
class Node:
    def __init__(self, data , next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DoubleLinkedList:
    lofl=0
    def __init__(self):
        self.root=None
        self.prev_root=None
        DoubleLinkedList.lofl=0
    def insert_beggining(self,data):
        node=Node(data,self.root,None)
        self.root=node
        if DoubleLinkedList.lofl==0:
            self.prev_root=node
        else:
            self.root.next.prev=node
        DoubleLinkedList.lofl+=1
    def print(self):
        if self.root is None:
            print('list empty')
            return
        itr=self.root
        while itr:
            print(str(itr.data)+" --> ",end='')
            itr= itr.next
        print()
    
    def print_behind(self):
        if self.prev_root is None:
            print('list empty')
            return
        itr=self.prev_root
        while itr:
            print(str(itr.data)+" --> ",end='')
            itr=itr.prev
        print()

    def insert_end(self,data):
        node=Node(data,None,self.prev_root)
        self.prev_root=node
        if DoubleLinkedList.lofl==0:
            self.root=node
        else:
            self.prev_root.prev.next=node
        DoubleLinkedList.lofl+=1

    def length(self):
        return DoubleLinkedList.lofl

    def decrease_length(self,num):
        DoubleLinkedList.lofl-=num

    def insert_pos(self,start,data,cursor):
        if cursor==-1:
            self.insert_beggining(data)
        elif cursor==self.length()-1:
            self.insert_end(data)
        else:
            node=Node(data,start.next,start.prev)
            temp=start
            start.next=node
            start=start.next.next
            start.prev=start.prev.next
            start=start.prev
            start.prev=temp
            
            DoubleLinkedList.lofl+=1

    def delete_next(self,pos):
        pos.next=pos.next.next
        pos=pos.next
        pos.prev=pos.prev.prev
        pos=pos.prev
        DoubleLinkedList.lofl-=1

    def delete_start(self,pos):
        self.root=pos.next
        pos=self.root
        pos.prev=pos.prev.prev
        DoubleLinkedList.lofl-=1
    
    def delete_end(self,pos):
        self.prev_root=pos
        pos.next=pos.next.next
        DoubleLinkedList.lofl-=1
