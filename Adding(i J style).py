Number2 = '700'
Number1= '300'
Sum=""
sum=0
j=len(Number2)-1
i=len(Number1)-1
temp=0
while i>=0 or j>=0:
    if i<0:
        sum=int(Number2[j])+temp
        temp=0
    if j<0:
        sum=int(Number1[i])+temp
        temp=0
    if j>=0 and i>=0:
        digit=int(Number1[i])
        digit1=int(Number2[j])
        sum=digit1+digit+temp
        temp=0
    if sum>9:
        sum=sum-10
        Sum=Sum+str(sum)
        temp=1
        if i<=0 and j<=0:
           Sum=Sum+str(temp)
    else: 
        Sum=Sum+str(sum)
    i-=1
    j-=1
Sum=Sum[::-1]
print(Sum)
    