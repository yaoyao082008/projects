from BSTs import BinarySearchTree
from queue import Queue


#nodes.get() dequeues
#nodes.put(x) enqueues

def levelOrder(root):
    nodes=Queue(maxsize=test.length)
    print(root.data,end='')
    itr=root
    nodes.put(root)
    count=0
    while count<test.length:
        itr=nodes.get()
        if itr.left:
            print(itr.left.data,end='')
            nodes.put(itr.left)
        if itr.right:
            print(itr.right.data,end='')
            nodes.put(itr.right)
        count+=1



test=BinarySearchTree(5)
test.insert(3)
test.insert(7)
test.insert(2)
test.insert(1)
test.insert(4)
test.insert(6)
test.insert(8)
levelOrder(test.root)