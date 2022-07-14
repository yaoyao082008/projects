from Double_LinkedList import *

class WordProcessor:
    def __init__(self):
        self.string=DoubleLinkedList()
        self.pos=self.string.root
        self.cursor=-1
    def insert_data(self,data):
        data=str(data)
        for i in range(len(data)):
            self.string.insert_pos(self.pos,data[i],self.cursor)
            if self.cursor==-1:
                self.pos=self.string.root
                self.cursor+=1
            else:
                self.move_cursor(1)

    def delete_data(self,distance):
        i=0
        if self.cursor==-1 and distance>=self.string.length():
            self.string=DoubleLinkedList()
            self.pos=self.string.root
            return
        elif self.pos.next==None: 
            return
        while i < distance-1 and self.pos.next.next:
            self.string.delete_next(self.pos)
            i+=1
        if self.cursor==self.string.length()-2:
            self.string.delete_end(self.pos)
        elif self.cursor==-1:
            self.string.delete_start(self.pos)
        else:
            self.string.delete_next(self.pos)

    def move_cursor(self,distance):
        if 0<=self.cursor+distance<self.string.length():
            if self.cursor==-1:
                distance-=1
                self.cursor+=1
            if distance>0:
                for i in range(distance):
                    self.pos=self.pos.next
            else:
                for i in range(-distance):
                    self.pos=self.pos.prev
            self.cursor+=distance
        elif distance<0:
            self.cursor=-1
            self.pos=self.string.root
        else:
            self.cursor=self.string.length()-1
            self.pos=self.string.prev_root
    def get_char(self,distance):
        data=''
        i=0
        if self.string.length()==0:
            return data
        elif self.cursor==-1:
            data+=self.pos.data
            distance-=1
            self.cursor+=1
        while i < distance and self.pos.next:
            self.move_cursor(1)
            data+=self.pos.data
            i+=1
        return data
        

text=WordProcessor()
text.insert_data('goodyaoyao')
text.move_cursor(5)
text.move_cursor(-3)
text.insert_data("zhou")
text.move_cursor(-7)
print(text.get_char(10))
text.move_cursor(10)
text.insert_data('goodjob')
text.move_cursor(-10)
text.delete_data(3)
print(text.get_char(10))

# for i in range(0):
#     text.insert_data(i+1)
# text.insert_data('101112')
# text.move_cursor(-6)
# text.delete_data(10)
# text.move_cursor(-10)
# text.move_cursor(-10)
# text.delete_data(10)
# text.insert_data('imback')
# text.move_cursor(-3)
# print(text.get_char(10))
# text.move_cursor(-10)
# text.delete_data(10)
# text.insert_data('hello')
# print("data:",text.pos.data)
# print("cursor:",text.cursor)
# text.string.print()
# text.string.print_behind()
# print(text.string.length())
