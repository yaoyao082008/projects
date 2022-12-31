from BinaryHeap import BinaryMinHeap

class node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class HuffmanCodeTree:
    def __init__(self,freq):
        self.words=BinaryMinHeap()
        self.tree1=None
        self.tree2=None
        self.total=None

        for key in freq.keys():
            self.words.insert([freq[key],key])

        self.build()

        

    def build(self):
        lfrequency,ldata=self.words.delete()
        rfrequency,rdata=self.words.delete()

        ldata=node(ldata)
        rdata=node(ldata)

        self.tree1=node(lfrequency+rfrequency,ldata,rdata)

        while self.words.size>2 and self.words.peek()[0]>=self.tree1.data:
            lfrequency,ldata=self.words.delete()
            ldata=node(ldata)
            self.tree1=node(lfrequency+self.tree1.data,ldata,self.tree1)


        lfrequency,ldata=self.words.delete()
        rfrequency,rdata=self.words.delete()

        ldata=node(ldata)
        rdata=node(rdata)

        self.tree2=node(lfrequency+rfrequency,ldata,rdata)

        while self.words.size>1:
            lfrequency,ldata=self.words.delete()
            ldata=node(ldata)
            self.tree2=node(lfrequency+self.tree2.data,ldata,self.tree2)

        if self.words.size==1:
            freq,data=self.words.storage.pop()
            data=node(data)
            if self.tree1.data<self.tree2.data:
                self.tree1=node(freq+self.tree1.data,data,self.tree1)
            else:
                self.tree2=node(freq+self.tree2.data,data,self.tree2)

        self.total=node(self.tree1.data+self.tree2.data,self.tree2,self.tree1)

    
    def map(self):
        pass