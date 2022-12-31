

def straight(dice):
    
    dice.sort()
    ans=0
    for i in range(len(dice)):
        if dice[i]>ans:
            ans+=1
    return ans





T=int(input())

for i in range(T):
    l=int(input())
    dices=input().split()
    for j in range(l):
        dices[j]=int(dices[j])

    ans=straight(dices)
    print('Case #'+str(i+1)+': ' ,str(ans))
