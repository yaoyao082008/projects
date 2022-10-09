

def fastest_speed(time):

    fastest=0
    for i in range(len(time)-1):
        curr_speed=abs(time[i+1][1]-time[i][1])/(time[i+1][0]-time[i][0])
        if curr_speed>fastest:
            fastest=curr_speed
    return fastest





num_observations=input()
time=[]
for i in range(int(num_observations)):
    time.append(input().split())
    time[i][0]=int(time[i][0])
    time[i][1]=int(time[i][1])

time.sort()

fastest=fastest_speed(time)
print(fastest)