



def check_magic(arr):
    total=0
    for i in range(4):
        total+=arr[i][0]

    for i in range(4):
        new_R=0
        new_C=0
        for j in range(4):
            new_R+=arr[i][j]
            new_C+=arr[j][i]
        if new_R!=total:
            return False
        if new_C!=total:
            return False
    return True
        
        

arr=[]


for i in range(4):
    row=input().split()
    for j in range(4):
        row[j]=int(row[j])
    arr.append(row)
    
val=check_magic(arr)

if val:
    print('magic')
else:
    print('not magic')
    
    
