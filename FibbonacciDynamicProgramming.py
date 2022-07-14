

def Fibonnaci(n):
    arr=[]
    arr.append(0)
    arr.append(1)
    for i in range(1,n):
        arr.append(arr[i]+arr[i-1])
    return arr[n]

print(Fibonnaci(10))