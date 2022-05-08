
#multiply by 3 to get how many digits in the next factorial
#work on 2 factorial and go to 3 then 4
#reversing is KEY
def all_permutations(Array,digits):
    if digits==1:
        return Array[len(Array)-1]
    for i in range(digits):
        pass
    return all_permutations(digits-1)

def create_Array(digits):
    Array=[0 for i in range(digits)]
    for i in range(digits):
        Array[i]=digits-i
    all_permutations(Array,digits)
print(create_Array(2))

