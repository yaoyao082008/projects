from linkedlist import LinkedList

class cache:
    def __init__(self,length):
        self.length=length
        self.storage=LinkedList()
        self.location={}
    
    def get(self,key=None):
        
        #get last value
        if key is None:
            return self.location.get('latest')

        if key not in self.location.keys():
            print(f'key {key} does not exist')
            return

        #update a key to latest
        orginal_node=self.location[key]

        #key value
        if orginal_node.next.next is None:
            return orginal_node.next.data[1]
        elif key==self.storage.root.data[0]:
            next=self.location[key].next
            key=self.location[key].data[0]
            value=self.location[key].data[1]
        else:
            key=self.location[key].next.data[0]
            value=self.location[key].next.data[1]
            next=self.location[key].next.next
        
        self.location[key]=self.storage.insert_end([key,value])
        self.location[next.data[0]]=self.storage.delete(key,orginal_node)

        self.location['latest']=[key,value]
        

        return value
        

    def insert(self,key,value):

        if key in self.location.keys():
            test.get(key)
            print(f'{key} is already in Database')
            return
        elif self.length==0:
            return
        
        self.location['latest']=[key,value]
        self.location[key]=self.storage.insert_end([key,value])

        # delete first value and update
        if self.storage.length >self.length:
            del self.location[self.storage.root.data[0]]
            new_root=self.storage.delete()
            self.location[new_root.data[0]]=new_root
        

    def print(self):
        self.storage.print()



test=cache(4)
test.get()
for i in range(4):
     test.insert(i+1,2*i+1)

test.insert(10, 11)
test.insert(13, 17)

print(test.get(13))
test.print()
print()