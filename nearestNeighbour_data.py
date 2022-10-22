from KD_TREE import KDTree
from medianOf2DArr import median
import csv
import time

start=time.time()


def construct(arr,start,end,layer):
    if end-start<=0:
        return

    mid=start+(end-start)//2

    median(arr,start,end,mid,layer)
    cars.insert(arr[mid])

    construct(arr,start+1,mid,layer^1)
    construct(arr,mid,end-1,layer^1)


cars=KDTree()
temp=[]

with open('sample_data.csv','r') as data:
    points=csv.reader(data)

    for point in points:
        x,y=float(point[0]),float(point[1])
        temp.append([x,y])

construct(temp,0,len(temp)-1,0)


with open('query_data.csv','r') as data:
    users=csv.reader(data)
    start=time.time()
    for user in users:
        x,y=float(user[0]),float(user[1])
        dis=cars.calc_dis((x,y),cars.root.coor)
        closet=cars.nearest_neighbour(cars.root,(x,y),(dis,0))
end=time.time()

print(end-start)