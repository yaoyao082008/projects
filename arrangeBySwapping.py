Array1=[0,1,2,0,1,1,0,2,0,1,0,2]
j=len(Array1)-1
Putinfront=0
i=0
while i <= j:
    if Array1[i]==0:
        Array1[i],Array1[Putinfront]=Array1[Putinfront],Array1[i]
        Putinfront+=1
        i+=1
    elif Array1[i]==2:
        Array1[i],Array1[j]=Array1[j],Array1[i]
        j-=1
    else:
        i+=1
    """if Putinfront-1==i:
        i+=1"""
for i in range(len(Array1)):
    print(Array1[i])
