

def AUXii_art(R,C):
    for i in range (2*R+1):
        for j in range(2*C+1):
            if i<2 and j<2:
                print('.',end='')
            elif i%2==0 and j%2==0:
                print('+',end='')
            elif i%2==0 and j%2!=0:
                print('-',end='')
            elif i%2!=0 and j%2==0:
                print('|', end='')
            elif i%2!=0 and j%2!=0:
                print('.',end='')
        print()



T=int(input())
for i in range(T):
    R=int(input())
    C=int(input())
    AUXii_art(R,C)