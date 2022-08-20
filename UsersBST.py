from BST_endtime import * 

def find_intervals(logs):
    total_users=0
    prev=logs.root
    
    while logs.has_next():
        current=logs.next()
        if prev!=current and current.users!=0:
            print(prev.data,'-',current.data,'=',total_users)
            prev=current
        total_users+=current.users

    print(prev.data,'- inf = 0')

        






logs=[[1,5],[1,6],[3,6],[7,9],[9,12]]

start=BinarySearchTree()

for i in range(len(logs)):
    if not start.search(logs[i][0],1):
        start.insert(logs[i][0],1)
    if not start.search(logs[i][1],-1):
        start.insert(logs[i][1],-1)

find_intervals(start)
    
