
def power(base,exponent):
    if(base==0):
        return 0
    res=1
    neg=0
    if(exponent<0):
        exponent=-exponent
        neg=1

    while exponent>0:
        if exponent%2==1:                 
            res=res*base
        base=base*base
        exponent = exponent//2

        """if posExponent%2==0:
            base=base*base
            posExponent/=2
        else:
            res=base*res
            posExponent-=1"""

    
    if(neg): 
        return 1/res
    return res
    

value=power(2,1)

print(value)


