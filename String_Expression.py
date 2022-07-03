from collections import deque

expression='(1+3/3-2)'
def solve_expression(expression):
    i=0
    term=0
    factor=1
    temp=0
    new=deque()
    while i < len(expression):
        if expression[i]==')':
            temp=new.pop()
            symbol=new.pop() 
            if symbol=='(':
                term=term+temp*factor
                i+=1
                new.append(term)
                factor=1
                term=0
            elif symbol=='*':
                factor=factor*temp
            elif symbol=='/':
                factor=factor*(1/temp)
            elif symbol=='+':
                term=term+temp*factor
                factor=1
            elif symbol=='-':
                term=term-temp*factor
                factor=1
        elif expression[i].isdigit():
            new.append(float(expression[i]))
            i+=1
        else:
            new.append(expression[i])
            i+=1
    return new

print(solve_expression(expression))