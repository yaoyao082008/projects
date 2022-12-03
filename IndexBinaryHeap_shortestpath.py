

class BinaryMinHeap:
    def __init__(self):
        self.storage=[]
        self.pm=[]
        self.map={}
        self.size=0

    def is_empty(self):
        return len(self.storage)==0

    def get_value(self,key):
        index=self.pm[self.map[key]]
        return self.storage[index][1]

    def poll(self):
        res=self.storage[0]
        self.size-=1
        del self.map[self.storage[0][0]]
        self.storage[0]=self.storage[-1]
        self.storage.pop()
        self.heapify_downIndex(0)
        return res


    def update(self,key,value):
        index=self.pm[self.map[key]]
        self.storage[index]=[key,value]
        self.heapify(index)

    def delete_key(self,key):
        self.size-=1
        index=self.pm[self.map[key]]
        self.swap(index,-1)
        self.storage.pop()
        self.heapify(index)
        del self.map[key]



    def peek(self):
        return self.storage[0]


    def insert(self,data):
        self.size+=1
        self.storage.append(data)
        self.pm.append(0)
        self.map[data[0]]=len(self.pm)-1
        self.heapify_upIndex(self.size-1)

    def heapify(self,index):
        if not self.has_parent(index):
            self.heapify_downIndex(0)
        elif self.storage[self.get_parent(index)][1]>self.storage[index][1]:
            self.heapify_upIndex(index)
        else:
            self.heapify_downIndex(index)
        


    def heapify_upIndex(self,index):
        self.pm[self.map[self.storage[index][0]]]=index
        while index > 0 and self.storage[index][1]<self.storage[self.get_parent(index)][1] :
            parent=self.get_parent(index)
            self.pm[self.map[self.storage[index][0]]]=parent
            self.pm[self.map[self.storage[parent][0]]]=index
            self.swap(index,parent)
            index=parent

    def heapify_downIndex(self,index):
        self.pm[self.map[self.storage[index][0]]]=index
        while self.has_left(index):
            child=self.get_left(index)
            if (self.has_right(index) and 
            self.get_right_data(index)[1]<self.get_left_data(index)[1]):
                child=self.get_right(index)
                self.pm[self.map[self.storage[child][0]]]=child
            if self.storage[index][1]<self.storage[child][1]:
                break
            self.pm[self.map[self.storage[index][0]]]=child
            self.pm[self.map[self.storage[child][0]]]=index
            self.swap(index,child)
            index=child

    def swap(self,index1,index2):
        self.storage[index1],self.storage[index2]=self.storage[index2],self.storage[index1]

    def swap_pm(self,index1,index2):
        key0=self.storage[index1][0]
        key1=self.storage[index2][0]
        self.pm[self.map[key0]],self.pm[self.map[key1]]=self.pm[self.map[key1]],self.pm[self.map[key0]]

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
        if (index-1)//2>=0:
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


# test = BinaryMinHeap()
# test.insert(['a',0])
# test.insert(['b',1])
# test.insert(['c',3])
# test.insert(['d',10])
# test.delete()
# test.insert(['e',0])
# test.insert(['f',12])
# test.insert(['g',15])
# test.insert(['h',16])
# test.update('h',-5)
# test.delete_key('d')
# print(test.storage)



