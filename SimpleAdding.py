Number2 = '9999'
Number1= '1'
Sum=""
sum=0
j=len(Number2)-1
i=len(Number1)-1
carrier=0
while i>=0 or j>=0:
    digit=0
    digit1=0
    if i>=0:
        digit=int(Number1[i])
    if j>=0:
        digit1=int(Number2[j])
    sum=digit1+digit+carrier
    if sum>9:
        sum=sum-10
        carrier=1
    else:
        carrier=0
    Sum=Sum+str(sum)
    i-=1
    j-=1
if carrier==1:
    Sum=Sum+str(carrier)
Sum=Sum[::-1]
print(Sum)
    