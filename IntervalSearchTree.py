

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.max=data[1]



class IntervalSearchTree:
    def __init__(self):
        self.root=None
        self.length=0

    def insert(self,data):
        self.length+=1
        if self.length==1:
            node=Node(data)
            self.root=node
            return
        itr=self.root
        while True:
            if data[1]>itr.max:
                itr.max=data[1]
            if data[0]>itr.data[0]:
                if not itr.right:
                    node=Node(data,None,itr.right)
                    itr.right=node
                    break
                itr=itr.right
            else:
                if not itr.left:
                    node=Node(data,itr.left,None)
                    itr.left=node
                    break
                itr=itr.left


    def search(self,interval):
        itr=self.root
        count=0
        while itr:
            if (itr.data[0]<interval[1]<=itr.data[1] 
            or itr.data[0]<interval[0]<itr.data[1]):
                count+=1
            if not itr.left or itr.left.max<=interval[0]:
                itr=itr.right
            else:
                itr=itr.left
        return count




    def in_order(self,root):
        if not root:
            return
        self.in_order(root.left)
        print('data: ',root.data[0],' max: ',root.max)
        self.in_order(root.right)
    



