
from collections import deque


class Node:
    def __init__(self,data,users,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.users=users


class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.length=0
        self.pos=self.root
        self.temp=[]

    def insert(self,data,users):
        self.length+=1
        if self.length==1:
            node=Node(data,users)
            self.root=node
            self.pos=self.root
            return
        itr=self.root
        while True:
            if data>itr.data:
                if not itr.right:
                    node=Node(data,users,None,itr.right)
                    itr.right=node
                    break
                itr=itr.right
            else:
                if not itr.left:
                    node=Node(data,users,itr.left,None)
                    itr.left=node
                    break
                itr=itr.left

    def search(self,data,users):
        itr=self.root
        while itr:
            if data>itr.data:
                itr=itr.right
            elif data<itr.data:
                itr=itr.left
            else:
                itr.users+=users
                return True
        return False



    def next(self):
        while True:
            if self.pos is not None:
                self.temp.append(self.pos)
                self.pos=self.pos.left
            elif self.temp:
                self.pos=self.temp.pop()
                val=self.pos
                self.pos=self.pos.right
                return val
            else:
                self.pos=self.root
                return

    def has_next(self):
        if self.pos is None and not self.temp:
            self.pos=self.root
            return False
        return True






    def in_order_w(self):
        stack = []
        while True:
            if self.pos is not None:
                stack.append(self.pos)
                self.pos=self.pos.left
            elif stack:
                self.pos = stack.pop()
                print(self.pos.data,self.pos.users)
                self.pos=self.pos.right
            else:
                self.pos=self.root
                break







    def pre_order(self,root):
        if not root:
            return
        print(root.data,end='')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self,state):
        if state:
            self.in_order(state.left)
            print(state.data)
            self.in_order(state.right)


    def post_order(self,root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data,end='')

    def pre_order_w(self):
        count=0
        itr=self.root
        temp=deque()
        while count<self.length:
            if not itr:
                itr=temp.pop()
                print(itr.data)
                itr=itr.right
            else:
                print(itr.data,end='')
                count+=1
                temp.append(itr)
                itr=itr.left
        print()

    
        

    def post_order_w(self):
        itr=self.root
        prev=self.root
        temp=deque()
        temp.append(self.root)
        while temp:
            if not itr:
                itr=temp[-1]
                if itr.right==prev or not itr.right:
                    prev=temp[-1]
                    print(temp.pop().data,end='')
                    itr=None #forms a loop to check for futrue prints
            else:
                if itr.right:
                    temp.append(itr.right)
                if itr.left:
                    temp.append(itr.left)
                itr=itr.left
        print()
    


