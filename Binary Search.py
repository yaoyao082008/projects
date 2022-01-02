Array=[1,2,4,5,7,11,100,113,200,250]
search=5
def sort(starting,ending,Spliting_Point):
    if Array[ending]==search:
        return ending
    if Array[starting]==search:
        return starting
    if  ending-starting>=1:
        if Array[Spliting_Point]==search:
            return Spliting_Point
        elif Array[Spliting_Point]<search:
            k=(ending-Spliting_Point)//2
            Spliting_Point=Spliting_Point+k
            return sort(Spliting_Point+1,ending,Spliting_Point+1)
        else:
            Spliting_Point=Spliting_Point//2
            if starting>Spliting_Point:
                return sort(Spliting_Point,starting, Spliting_Point)
            else:
                return sort(starting,Spliting_Point, Spliting_Point)
    else:
        return -1
        




k=sort(0,len(Array)-1,(len(Array)-1)//2)
print(k)