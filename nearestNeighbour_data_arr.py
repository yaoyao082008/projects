from arr_kdTree import kdTree
from KD_TREE import KDTree
import csv
import time

cars=kdTree()
test=KDTree()


with open('sample_data.csv','r') as data:
    points=csv.reader(data)

    for point in points:
        x,y=float(point[0]),float(point[1])
        cars.insert([x,y])
        test.insert([x,y])


with open('query_data.csv','r') as data:
    users=csv.reader(data)
    start=time.time()
    for user in users:
        x,y=float(user[0]),float(user[1])
        dis=cars.calc_dis((x,y),cars.tree[0])
        closet=cars.nearest_neighbour(0,(x,y),(dis,0))
        b=test.nearest_neighbour(test.root,(x,y),(dis,0))
        if closet[0]==b[0]:
            print('prssed')
        else:
            print('u bad')


end=time.time()

print(end-start)