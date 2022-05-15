def permutation(start,Array):
    if start==len(Array)-1:
        print(Array)
        return Array
    for i in range(start,len(Array)):
        b=Array.copy()
        b[i],b[start]=b[start],b[i]
        permutation(start+1,b)

        
#[1,2,3]
num=5
A=[i for i in range(1,num+1)]
permutation(0,A)


