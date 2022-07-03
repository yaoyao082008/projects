
def TowerOfHanoi(n , source, destination, auxiliary):
    global times
    if n==1:
        times+=1
        print (times,"Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    times+=1
    print (times,"Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n=15
times=0
TowerOfHanoi(n,'A','B','C')
