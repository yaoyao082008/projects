
digits=[9,9]

for i in range(len(digits)-1,-1,-1):
    if digits[i]==9:
        digits[i]=0
    else:
        digits.insert(i,1)
        break
    
digits.insert(0,1)