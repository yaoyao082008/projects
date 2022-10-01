from math import sqrt


class Node:
    def __init__(self,coor,left=None,right=None):
        self.coor=coor
        self.left=left
        self.right=right

class kdTree:
    
    def __init__(self):
        self.root=None

    def insert(self,coor):
        if self.root is None:
            self.root=Node(coor)
            return

        layer=0
        itr=self.root
        while coor!=itr.coor:
            if coor[layer]>itr.coor[layer]:
                if not itr.right:
                    itr.right=Node(coor,None,itr.right)
                    break
                itr=itr.right
            else:
                if not itr.left:
                    itr.left=Node(coor,itr.left)
                    break
                itr=itr.left
            layer=layer^1     



    def insert_rec(self,coor,root,layer=0):
        if root is None:
            return

        if coor[layer]>root.coor[layer]:
            self.insert_rec(coor,root.right,layer^1)
            root.right=Node(coor)
        else:
            self.insert_rec(coor,root.left,layer^1)
            root.left=Node(coor)
        



    def nearest_neighbour(self,root,coor,best_distance,layer=0):
        if root is None:
            return best_distance

        distance=(self.calc_dis(coor,root.coor),root.coor)

        if distance[0]<best_distance[0]:
            best_distance=distance

        if coor[layer]<root.coor[layer]:
            next=root.left
            other=root.right
        else:
            next=root.right
            other=root.left

        best_curr=self.nearest_neighbour(next,coor,best_distance,1-layer)

        perpendic_dis=coor[layer]-root.coor[layer]

        if perpendic_dis<best_curr[0]:
            best_other=self.nearest_neighbour(other,coor,best_curr,1-layer)
            if best_other[0]<best_curr[0]:
                return best_other
        return best_curr



    def brute_force(self,root,coor,best_dis):
        if not root:
            return best_dis
        distance=(self.calc_dis(coor,root.coor),root.coor)
        if distance[0]<=best_dis[0]:
            best_dis=distance
        best1=self.brute_force(root.left,coor,best_dis)
        best2=self.brute_force(root.right,coor,best_dis)

        if best1[0]<best2[0]:
            return best1
        return best2    

    @staticmethod
    def calc_dis(coor0,coor1):
        x1,y1=coor0
        x2,y2=coor1
        return sqrt((x2-x1)**2 + (y2-y1)**2)




"""test=kdTree()
test.insert([5,4])
test.insert([2,6])
test.insert([13,3])
test.insert([3,1])
test.insert([10,2])
test.insert([8,7])
test.insert([9,3])

print()
query_point=[9,4]
nearest=test.nearest_neighbour(test.root,query_point,(test.calc_dis(query_point,test.root.coor),0))
print(nearest)"""