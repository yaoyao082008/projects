

from math import sqrt


class kdTree:

    def __init__(self):
        self.tree=[None for i in range(2240)]



    def insert(self,coor):
        index=0
        if self.tree[index] is None:
            self.tree[0]=coor
            return
        layer=0

        while coor!=self.tree[index]:
            if coor[layer]>self.tree[index][layer]:
                if self.tree[self.right(index)] is None:
                    self.tree[self.right(index)]=coor
                    break
                index=self.right(index)
            else:
                if self.tree[self.left(index)] is None:
                    self.tree[self.left(index)]=coor
                    break
                index=self.left(index)
            layer=1-layer

        


    def nearest_neighbour(self,index,coor,best_distance,layer=0):
        if index is None or self.tree[index] is None:
            return best_distance

        distance=(self.calc_dis(coor,self.tree[index]),self.tree[index])

        if distance[0]<best_distance[0]:
            best_distance=distance

        if coor[layer]<self.tree[index][layer]:
            next=self.left(index)
            other=self.right(index)
        else:
            next=self.right(index)
            other=self.left(index)

        best_curr=self.nearest_neighbour(next,coor,best_distance,1-layer)

        perpendic_dis=coor[layer]-self.tree[index][layer]

        if perpendic_dis<best_curr[0]:
            best_other=self.nearest_neighbour(other,coor,best_curr,1-layer)
            if best_other[0]<best_curr[0]:
                return best_other
        return best_curr

    @staticmethod
    def calc_dis(coor1,coor2):
        x1,y1=coor1
        x2,y2=coor2
        return sqrt((x2-x1)**2+(y2-y1)**2)


    def left(self,index):
        i=index*2+1
        if i>=len(self.tree):
            return 
        return i

    def right(self,index):
        i=index*2+2
        if i>=len(self.tree):
            return 
        return i