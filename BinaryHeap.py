

class BinaryMinHeap:
    def __init__(self):
        self.storage=[]
        self.size=0


    def delete(self):
        self.storage[0]=self.storage[-1]
        self.storage.pop()
        self.heapify_down()


    def heapify_down(self):
        index=0
        while (self.has_left(index) ):
            child=self.get_left(index)
            if (self.has_right(index) and 
            self.get_right_data(index)<self.get_left_data(index)):
                child=self.get_right(index)
            if self.storage[index]<self.storage[child]:
                break
            self.swap(index,child)
            index=child


    def peek(self):
        return self.storage[0]


    def insert(self,data):
        self.storage.append(data)
        self.size+=1
        self.heapify_up()
        

    def heapify_up(self):
        track=len(self.storage)-1
        while track > 0 and self.storage[track]<self.storage[self.get_parent(track)] :
            k=self.get_parent(track)
            self.storage[track],self.storage[k]=self.storage[k],self.storage[track]
            track=k


    def swap(self,index1,index2):
        self.storage[index1],self.storage[index2]=self.storage[index2],self.storage[index1]

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

    def has_parent(self,index):
        if (index-1)//2>=0 or (index-1)//2<self.size:
            return True
        return False

    def has_left(self,index):
        if index*2+1<self.size:
            return True
        return False
    def has_right(self,index):
        if index*2+2<self.size:
            return True
        return False


test = BinaryMinHeap()
test.insert(0)
test.insert(1)
test.insert(2)
test.storage[0]=3
test.heapify_down()
print(test.storage)



