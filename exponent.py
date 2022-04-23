
def power(base,exponent):
    posExponent=abs(exponent)
    res=1

    if(base==0):
        return 0

    while posExponent>0:
        if posExponent%2==1:
            res=base*res
        base=base*base
        posExponent//=2

    if exponent<0:
        return 1/res
    return res

value=power(2,11)

print(value)


