Number1=0
Number2=1
Sum=0
length=18
for i in range(length):
    Sum=Number1+Number2
    if i == length-1:
        print(Sum)
    Number1=Number2
    Number2=Sum