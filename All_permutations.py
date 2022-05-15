def permutation(start,num,Array):
    k=num-1
    if start==0:
        return Array
    for i in range(num):
        Array[i+start],Array[k]=Array[k],Array[i+start]
        k-=1
        print(Array)
        if start>1:
            return permutation(start-1,num,Array)
        elif start<1:
            return permutation(start+1,num,Array)
    
num=4
A=[i for i in range(num,0,-1)]
permutation(len(A)-1,num,A)


