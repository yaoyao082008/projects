
def next_permutation(Array):
    Biggest_permuation_ends=0
    for i in range(len(Array)-1,0,-1):
        if Array[i]>Array[i-1]:
            Biggest_permuation_ends=i-1
            break
    for i in range(len(Array)-1,0,-1):
        if Array[i]>Array[Biggest_permuation_ends]:
            Array[i],Array[Biggest_permuation_ends]=Array[Biggest_permuation_ends],Array[i]
            Biggest_permuation_ends+=1
            break
    reverse(Biggest_permuation_ends,len(Array)-1,Array)



def reverse(Biggest_permuation_ends,end,Array):
    for i in range((len(Array)-Biggest_permuation_ends)//2):
        Array[Biggest_permuation_ends],Array[end]=Array[end],Array[Biggest_permuation_ends]
        end-=1
        Biggest_permuation_ends+=1

Array=[1,3,2,5,6,4]
# for i in range(24):
next_permutation(Array)
print(Array)