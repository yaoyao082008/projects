from KD_TREE import kdTree
import csv
import time

cars=kdTree()





with open('sample_data.csv','r') as data:
    points=csv.reader(data)

    for point in points:
        x,y=float(point[0]),float(point[1])
        cars.insert([x,y])


with open('query_data.csv','r') as data:
    users=csv.reader(data)
    start=time.time()
    for user in users:
        x,y=float(user[0]),float(user[1])
        dis=cars.calc_dis((x,y),cars.root.coor)
        closet=cars.nearest_neighbour(cars.root,(x,y),(dis,0))
        #force=cars.brute_force(cars.root,(x,y),(dis,0))
end=time.time()

print(end-start)