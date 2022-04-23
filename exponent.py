
def power(base,exponent):
    posExponent=abs(exponent)
    mainVar=base
    storedVar=1

    if(base==0):
         return 0

    while posExponent>1:
        if posExponent%2==0:
            mainVar=mainVar*mainVar
            posExponent=posExponent/2
        else:
            storedVar=mainVar*storedVar
            posExponent-=1

    if exponent<0:
        return 1/(mainVar*storedVar)
    elif exponent>0:
        return mainVar*storedVar
    else:
        return 1

value=power(2,9)

print(value)


