
from collections import deque


class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right



class BinarySearchTree:
    def __init__(self,data):
        self.root=Node(data)
        self.length=1
    def insert(self,data):
        itr=self.root
        self.length+=1
        while True:
            if data>itr.data:
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


    def pre_order(self,root):
        if not root:
            return
        print(root.data,end='')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self,root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)

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

    def in_order_w(self):
        count=0
        itr=self.root
        temp=deque()
        while count<self.length:
            if not itr:
                itr=temp.pop()
                print(itr.data,end='')
                count+=1
                itr=itr.right
            else:
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
                    itr=None
            else:
                if itr.right:
                    temp.append(itr.right)
                if itr.left:
                    temp.append(itr.left)
                itr=itr.left
        print()
    


    
            



test=BinarySearchTree(5)
test.insert(3)
test.insert(7)
test.insert(4)
test.insert(2)
test.insert(1)
test.insert(6)
test.insert(12)
test.insert(8)
test.insert(10)
test.insert(11)
test.insert(13)
test.insert(0)
test.post_order_w()
