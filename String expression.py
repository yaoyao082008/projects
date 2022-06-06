Expression=['2','*','3','*','6','/','2','+','6','*','2','-','4','/','2','-','2','*','2','*','2','*','2','*','2','*','2']
nums='123+4+5+5'
k=0
i=1
while len(Expression)>1:
    if (Expression[i]=='-' and i+2>=len(Expression)
     or Expression[i]=='-' and Expression[i+2]!='*' 
     and Expression[i+2]!='/'):
        Expression[i]= float(Expression[i-1])-float(Expression[i+1])
        del Expression[i-1],Expression[i]
        i=-1

    elif (Expression[i]=='+' and i+2>=len(Expression) 
    or Expression[i]=='+' and Expression[i+2]!='*' 
    and Expression[i+2]!='/'):
        Expression[i]=float(Expression[i-1])+float(Expression[i+1])
        del Expression[i-1],Expression[i]
        i=-1

    elif Expression[i]=='*':
        Expression[i]=float(Expression[i-1])*float(Expression[i+1])
        del Expression[i-1],Expression[i]
        i=-1

    elif Expression[i]=='/':
        Expression[i]=float(Expression[i-1])/float(Expression[i+1])
        del Expression[i-1],Expression[i]
        i=-1
    i+=2
print(Expression)