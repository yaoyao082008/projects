
class Node:
    def __init__(self, data , next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.root=None
        self.length=0

    def insert_beggining(self,data):
        node=Node(data,self.root)
        self.root=node
        self.length+=1
    def print(self):
        if self.root is None:
            print('list empty')
            return
        itr=self.root
        while itr:
            print(str(itr.data)+" --> ",end='')
            itr= itr.next
        print()


    def insert_end(self,data):
        node=Node(data,None)
        self.length+=1
        if self.root is None:
            self.root=node
            return
        itr=self.root
        while itr.next:
            itr=itr.next
        itr.next=node


    def len(self):
        return self.length

    def delete(self,index):
        if index<0 or index>= self.length():
            print('not valid')
            return
        self.length-=1
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
        if index<0 or index>= self.length:
            print('not valid')
            return
        self.length+=1
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
                self.length-=1
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
                self.length+=1
                return
            itr=itr.next
        print('no value found')
        return
    


