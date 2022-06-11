
Expression='69+42*8/4+3'

num=[]
symbol=''
k=0
prev_k=0

for i in range(len(Expression)):
    if Expression[i].isdigit():
        num.append(Expression[i])
        k+=1
    if not Expression[i].isdigit():
        num[prev_k:k]=[''.join(num[prev_k:k])]
        num.append(Expression[i])
        prev_k=len(num)
        k=prev_k

num[prev_k:k]=[''.join(num[prev_k:k])]
k=0
i=1
while len(num)>1:
    if (num[i]=='-' and i+2>=len(num)
     or num[i]=='-' and num[i+2]!='*' 
     and num[i+2]!='/'):
        num[i]= float(num[i-1])-float(num[i+1])
        del num[i-1],num[i]
        i=-1

    elif (num[i]=='+' and i+2>=len(num) 
    or num[i]=='+' and num[i+2]!='*' 
    and num[i+2]!='/'):
        num[i]=float(num[i-1])+float(num[i+1])
        del num[i-1],num[i]
        i=-1

    elif num[i]=='*':
        num[i]=float(num[i-1])*float(num[i+1])
        del num[i-1],num[i]
        i=-1

    elif num[i]=='/':
        num[i]=float(num[i-1])/float(num[i+1])
        del num[i-1],num[i]
        i=-1
    i+=2
print(num)
