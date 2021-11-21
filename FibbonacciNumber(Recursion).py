def FN(n):
    if n ==1:
        return 1
    if n==0:
        return 0
    fnMinus2=FN(n-2)
    fnMinus1=FN(n-1)
    return fnMinus2+fnMinus1

k=FN(19)
print(k)
