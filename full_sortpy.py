array1=[0,1,1,2,0,1,2,0,1,4,4,5,8,6,6,6,4,4,4,8,8]
def sort(starting,ending,array1):
    if  ending-starting<=1:
        return
    Spliting_Point=starting+1
    for i in range(starting ,ending):
        if array1[i]<array1[starting]:
            array1[i],array1[Spliting_Point]=array1[Spliting_Point],array1[i]
            Spliting_Point+=1
    Spliting_Point-=1
    array1[starting],array1[Spliting_Point]=array1[Spliting_Point],array1[starting]
    sort(starting,Spliting_Point,array1)
    sort(Spliting_Point+1,ending,array1)



sort(0,len(array1), array1)
     
for i in range(len(array1)):
    print(array1[i])