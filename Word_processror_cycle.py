from DoubleLinkedListCycle import *

class WordProcessor:
    def __init__(self):
        self.string=DoubleLinkedListCycle()
        self.pos=self.string.root
        self.cursor=0
    def insert_data(self,data):
        data=str(data)
        for i in range(len(data)):
            self.string.insert_at(data[i],self.pos,self.cursor)
            self.move_cursor(1)

    def delete_data(self,distance):
        i=0
        while i<distance and self.pos.next!=self.string.root:
            self.string.delete_at(self.pos,self.cursor)
            i+=1

    def move_cursor(self,distance):
        i=0
        if self.pos==None:
            self.pos=self.string.root
            return
        if distance>0:
            while i< distance and self.pos.next!= self.string.root:
                self.pos = self.pos.next
                i+=1
                self.cursor+=1
        elif distance<0:
            while i<-distance and self.pos.prev!=self.string.root.prev:
                self.pos=self.pos.prev
                i+=1
                self.cursor-=1
        return self.pos.data
        
    def get_char(self,distance):
        data=''
        for i in range(distance):
            data+=self.move_cursor(1)
        return data
        

text=WordProcessor()
text.insert_data('1234')
text.move_cursor(-10)
text.delete_data(10)
print(text.cursor)
print(text.pos.data)
text.string.print_ll()
