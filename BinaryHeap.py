class BinaryMinHeap:
    def __init__(self):
        self.storage=[]
        self.size=0


    def delete(self):
        self.storage[0]=self.storage[-1]
        self.storage.pop()
        self.size-=1
        track=0
        while (self.storage[track]>self.get_left_data(track) or 
        self.storage[track]>self.get_right_data(0)):
            if self.storage[track]>self.get_left_data(track):
                k=self.get_left(track)
                self.storage[track],self.storage[k]=self.storage[k],self.storage[track]
                track=k

            elif self.storage[track]>self.get_right_data(0):
                k=self.get_right(track)
                self.storage[track],self.storage[k]=self.storage[track],self.storage[k]
                track=k

        


    def insert(self,data):
        self.storage.append(data)
        track=len(self.storage)-1
        self.size+=1
        while track > 0 and self.storage[track]<self.storage[self.get_parent(track)] :
            k=self.get_parent(track)
            self.storage[track],self.storage[k]=self.storage[k],self.storage[track]
            track=k


    def get_parent_data(self,index):
        return self.storage[self.get_parent(index)]


    def get_left_data(self,index):
        return self.storage[self.get_left(index)]

    def get_right_data(self,index):
        return self.storage[self.get_right(index)]

    def get_parent(self,index):
        return (index-1)//2

    def get_left(self,index):
        return 2*index+1

    def get_right(self,index):
        return 2*index+2



test=BinaryMinHeap()
for i in range(4):
    test.insert(i+1)
test.insert(0)
test.delete()
print(test.storage)