

def num_of_ways(num):
    count=1
    total=0
    while num>=0:
        if num%4==0:
            total+=1
        num-=5


    return total

num=int(input())
print(num_of_ways(num))

