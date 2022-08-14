from BST_endtime import * 

def find_intervals(logs):
    logs.in_order_w()





logs=[[1,5],[1,6],[3,6],[7,9]]

start=BinarySearchTree()

for i in range(len(logs)):
    if not start.search(logs[i][0],1):
        start.insert(logs[i][0],1)
    if not start.search(logs[i][1],-1):
        start.insert(logs[i][1],-1)

find_intervals(start)
    
