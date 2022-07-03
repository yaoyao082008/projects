
#1,5,10

count=0
num=17

temp=num%10
num=num-temp
count+=(num/10)
count+=temp%5
temp-=temp%5
temp=temp/5
count+=temp



print(count)



