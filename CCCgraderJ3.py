

def output(tuning):
    inst=''
    left_off=0
    curr=0
    digits=''
    i=0
    while i<len(tuning):
        if tuning[i]=='+':
            inst='tighten'
            curr=i-1
        elif tuning[i]=='-':
            inst='loosen'
            curr=i-1
        elif tuning[i].isdigit():
            digits+=tuning[i]
        if i==len(tuning)-1 or tuning[i].isdigit() and tuning[i+1].isalpha():
            print(tuning[left_off:curr+1],inst,digits)
            left_off=i+1
            digits=''
        i+=1









tuning=input()
output(tuning)

