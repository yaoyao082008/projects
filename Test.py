Array=[1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1]
start=0
for i in range(len(Array)):
    if Array[i]==1:
        Array[start],Array[i]=Array[i],Array[start]
        start+=1

print(Array)