
class Node:
    def __init__(self, data , next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.root=Node(['r','r'],None)
        self.length=0


    def insert_end(self,start,data):
        node=Node(data,None)
        self.length+=1
        if self.root is None:
            self.root.next=node
            return self.root

        start.next=node
        return start



    def print(self):
        if self.root is None:
            print('list empty')
            return
        itr=self.root.next
        while itr:
            print(str(itr.data)+" --> ",end='')
            itr= itr.next
        print()


    def len(self):
        return self.length

    def delete(self,node=None):
        self.length-=1

        if node is None or node.data==self.root.data:
            self.root.next=self.root.next.next
            return self.root.next

        
        node.next=node.next.next

        return node


test=LinkedList()
previous=test.insert_end(5)
print()



    

