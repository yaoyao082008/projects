Array=[1,7,9,10,12,15,3,2]


def selection_sort(Array):
    for i in range(len(Array)):
        minium=i
        for j in range(i,len(Array)):
            if Array[minium]>Array[j]:
                minium=j
                print(minium)
        Array[minium],Array[i]=Array[i],Array[minium]

    return Array
    #minium=i+1
def bubble_sort(Array):
    for i in range(len(Array)-1):
        for j in range(len(Array)-i-1):
            if Array[j]>Array[j+1]:
                Array[j],Array[j+1]=Array[j+1],Array[j]
    return Array

def insertion_sort(Array):
    for i in range(len(Array)-1):
        curNum,preIndex=Array[i+1],i
        while preIndex>0 and curNum<Array[preIndex]:
            Array[preIndex+1]=Array[preIndex]
            preIndex-=1
        Array[preIndex+1]=curNum
    return Array
                

print(insertion_sort(Array))
            
