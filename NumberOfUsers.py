
def find_intervals(logs):
    logs.sort()
    count=1
    repeats={}
    for i in range(len(logs)):
        if i+1<len(logs) and logs[i][0]==logs[i+1][0]:
            count+=1
            repeats[logs[i][0]]=count
        else:
            repeats[logs[i][0]]=count
            count=1
    users=0
    line=logs[0][0]
    start=0
    prev=repeats[logs[0][0]]
    p=logs[0][0]
    while logs:
        for i in range(start):
            if line>=logs[i][1]:
                users-=1
                start-=1
                del logs[i]
                break
        if start<len(logs) and line>=logs[start][0]:
            users+=repeats[logs[start][0]]
            start+=repeats[logs[start][0]]
        if prev!=users:
            print(p,'-',line,'=',prev)
            p=line
        prev=users
        line+=1
    print(p,'- inf = 0')
    
logs=[[2,4],[1,6],[3,5],[4,8]]
find_intervals(logs)