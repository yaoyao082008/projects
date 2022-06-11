Number2 = '1920'
Number1= '321'
Sum=""
temp=0
if len(Number1)>len(Number2):
    longer=Number1
    smaller=Number2
else:
   longer=Number2
   smaller=Number1
for i in range(len(longer)):
    if len(smaller)-i-1<0:
        sum=int(longer[len(longer)-i-1])+temp
        temp=0
    else:
        digit=int(Number1[len(Number1)-1-i])
        digit1=int(Number2[len(Number2)-1-i])
        sum=digit1+digit+temp
        temp=0
    if sum>9:
        sum=sum-10
        Sum=Sum+str(sum)
        temp=1
        if len(longer)-i-1==0:
            Sum=Sum+str(temp)
    else: 
        Sum=Sum+str(sum)
Sum=Sum[::-1]
print("")
print(Sum)
    