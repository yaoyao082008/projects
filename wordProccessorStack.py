from collections import deque

from pkg_resources import working_set



class WordProcessor:
    def __init__(self):
        self.string=deque()
        self.temp=deque()
    def move_cursor(self,distance):
        i=0
        if distance>0:
            while i<distance and len(self.temp)>0:
                self.string.append(self.temp.pop())
                i+=1
            return self.string[-1]
        while i < -distance and len(self.string)>0:
            self.temp.append(self.string.pop())
            i+=1
    def insert_data(self,data):
        data=str(data)
        for i in range(len(data)):
            self.string.append(data[i])
    def delete_data(self,distance):
        i=0
        while i<distance and len(self.temp)>0:
            self.temp.pop()
            i+=1
    def get_char(self,distance):
        i=0
        while i<distance and len(self.temp)>0:
            print(self.move_cursor(1),end='')
        print()
text=WordProcessor()
text.insert_data('123456789')
text.move_cursor(-10)
text.get_char(10)
text.move_cursor(-4)
text.delete_data(10)
text.move_cursor(-10)
text.get_char(10)
print(text.string)
print(text.temp)
    
        