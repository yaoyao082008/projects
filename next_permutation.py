Array=[1,4,3,2]
switch=False
#smallest number greater than I
#we know to change the thousands digit if there is no digit greater than the hundreds
#right after you swap with the hundreds the tens and ones also swap
#the biggest permutation is when a number is in ascending order
#find a number then swap it
def next_permutation():
    place=len(Array)-1
    end=place
    done=False
    for i in range(len(Array)-1,-1,-1):
        if Array[i]>Array[i-1]:
            end=i-1
            done=True
        if Array[place]<Array[end]:
            place-=1
        if done:
            Array[place],Array[end]=Array[end],Array[place]
            break
    rev=len(Array)-1
    end+=1
    for i in range(end,len(Array)//2):
        Array[end],Array[rev]=Array[rev],Array[end]
        rev-=1


next_permutation()
print(Array)
