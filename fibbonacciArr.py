import time
start=time.time()
def Fibonacci(n):
    memo=[0]*(n+1)
    memo[0],memo[1]=0,1
    for i in range(2,n+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n]

def Find_Steps(n):
    res=[0]*(n+2)
    res[0]=1
    res[1]=1
    res[2]=2
    for i in range(3,n+1):
        res[i]=res[i-1]+res[i-2]+res[i-3]
    return res[n]
print(Find_Steps(5))
end=time.time()
print(end-start)