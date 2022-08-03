from BST_endtime import * 

def find_intervals(root):
    if not root:
        return
    find_intervals(root.left)
    print(root.data,root.users)
    find_intervals(root.right)
    
logs=[[0,3],[0,4],[1,5],[1,6],[3,6]]
start=BinarySearchTree()
for i in range(len(logs)):
    if not start.search(logs[i][0],1):
        start.insert(logs[i][0],1)
    if not start.search(logs[i][1],-1):
        start.insert(logs[i][1],-1)
find_intervals(start.root)
