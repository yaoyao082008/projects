from Double_LinkedList_cacheProblem import DoubleLinkedListCycle

class cache:
    def __init__(self,length):
        self.length=length
        self.storage=DoubleLinkedListCycle()
        self.location={}
    
    def get(self,key=None):
        
        #get last value
        if key is None:
            if self.storage.is_empty():
                return
            return self.storage.root.prev.data

        if key not in self.location.keys():
            print(f'key {key} does not exist')
            return

        #update a key to latest
        orginal_node=self.location[key]
        value=self.location[key].data[1]

        # #key value
        # if orginal_node.next.next ==self.storage.root:
        #     return orginal_node.next.data[1]

        self.storage.insert_end([key,value])
        self.storage.delete(orginal_node)


        return value
        

    def insert(self,key,value):

        if key in self.location.keys():
            test.get(key)
            print(f'{key} is already in Database')
            return
        elif self.length==0:
            return
        
        self.location[key]=self.storage.insert_end([key,value])

        # delete first value and update
        if self.storage.length >self.length:
            del self.location[self.storage.root.data[0]]
            self.storage.delete()
        

    def print(self):
        self.storage.print()



test=cache(4)
#test.get()
for i in range(4):
     test.insert(i+1,2*(i+1))

test.insert(10, 11)
test.insert(13, 17)

print(test.get(13))
print(test.get(3))
print(test.get(3))
test.insert(10,12)
print(test.get())
test.print()
print()