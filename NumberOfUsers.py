from collections import deque


def find_intervals(logs):
    logs.sort()
    latest_log=deque()
    latest_log.append(logs[0][0])
    count=0
    for i in range(len(logs)-1):
        start=latest_log.pop()
        if logs[i][1]==logs[i+1][0]:
            latest_log.append(logs[i+2][0])
            count+=1
            print('[',start,',',latest_log[-1],') --->', count)
        elif True:
            pass







logs=[[6,9],[0,3],[5,8],[3,7]]
logs.sort()
print(logs)
#find_intervals(logs)

