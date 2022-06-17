from collections import deque
Expression='6+((1+3)/4*(2+6))/(3+6)*(2+3*2)'
def solve_string_expression(Expression,start,end): 
    symbol=deque()
    numbers=deque()
    i=start
    while i<end:
        curr = Expression[i]
        if curr=='*':
            numbers.append(numbers.pop()*float(Expression[i+1]))
            i+=1
        elif curr=='/':
            numbers.append(numbers.pop()/float(Expression[i+1]))
            i+=1
        elif curr=='+' or curr=='-':
            symbol.append(curr)
        else:
            numbers.append(float(curr)) 
        i+=1

    while len(symbol)>0:
        curr=symbol.pop()
        n1=numbers.pop()
        n2=numbers.pop()
        if( curr=='+'):
            numbers.append(n1+n2)
        else:
            numbers.append(n2-n1)
    return numbers.pop()




track_paranthesse=deque()
new=deque()
for i in range (len(Expression)):
    curr=Expression[i]
    if curr=='(':
        new.append(curr)
        track_paranthesse.append(len(new))
    elif curr==')':
        k=solve_string_expression(new,track_paranthesse[-1],len(new))
        for j in range(track_paranthesse.pop(),len(new)):
            new.pop()
        new[-1]=k
    elif curr.isdigit():
        new.append(float(Expression[i]))
    else:
        new.append(Expression[i])

solution=solve_string_expression(new,0,len(new))
print(solution)