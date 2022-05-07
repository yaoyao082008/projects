Array=[1,2,3,4]
switch=False
def next_permutation():
    Biggest_permuation_ends=0
    swap=0
    k=len(Array)-1
    for i in range(len(Array)-1,0,-1):
        if Array[i]>Array[i-1]:
            Biggest_permuation_ends=i-1
            break
    for i in range(len(Array)-1,-1,-1):
        if Array[i]>Array[Biggest_permuation_ends]:
            swap=i
            Array[swap],Array[Biggest_permuation_ends]=Array[Biggest_permuation_ends],Array[swap]
            Biggest_permuation_ends+=1
            break
    reverse(Biggest_permuation_ends,k)





def reverse(Biggest_permuation_ends,k):
    for i in range((len(Array)-Biggest_permuation_ends)//2):
        Array[Biggest_permuation_ends],Array[k]=Array[k],Array[Biggest_permuation_ends]
        k-=1
        Biggest_permuation_ends+=1
next_permutation()
print(Array)