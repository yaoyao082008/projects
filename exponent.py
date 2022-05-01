
def power(base,exponent):
    posExponent=abs(exponent)
    res=1

    if(base==0):
        return 0

    while posExponent>0:
        if posExponent%2==1:
            res=base*res
        base=base*base
        posExponent= posExponent>>1

    if exponent<0:
        return 1/res
    return res

value=power(9,12)

print()


