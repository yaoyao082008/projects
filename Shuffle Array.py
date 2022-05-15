Array=[1,2,3,4]
start=0
num=len(Array)
k=num-1
for i in range((num-start)//2):
        Array[i+start],Array[k]=Array[k],Array[i+start]
        k-=1

print(Array)
