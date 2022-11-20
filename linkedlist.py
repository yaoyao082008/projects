
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

    def insert_end(self,data):
        node=Node(data,None)
        self.length+=1
        if self.root is None:
            self.root=node
            return node

        itr=self.root
        while itr.next:
            itr=itr.next
        itr.next=node

        return itr



    def print(self):
        if self.root is None:
            print('list empty')
            return
        itr=self.root
        while itr:
            print(str(itr.data)+" --> ",end='')
            itr= itr.next
        print()


    def len(self):
        return self.length

    def delete(self,org=None,node=None):
        self.length-=1

        if node is None and org is None    or org==node.data[0]:
            self.root=self.root.next
            return self.root

        
        temp=node.next.next
        trash=node.next
        node.next.next=None
        node.next=temp
        del trash

        return node


        
    
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


    

