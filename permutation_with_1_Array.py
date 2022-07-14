def permutation(start,Array):
    if start==len(Array)-1:
        print(Array)
        return Array
    for i in range(start,len(Array)):
        Array[i],Array[start]=Array[start],Array[i]
        permutation(start+1,Array)
        Array[i],Array[start]=Array[start],Array[i]
num=3
A=[i for i in range(1,num+1)]
permutation(0,A)