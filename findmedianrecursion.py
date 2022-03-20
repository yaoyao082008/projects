Array1=[1,3,8,9]
Array2=[4,5,7,10]
eliminate_start= (len(Array1)+len(Array2)-1)//2
eliminate_end= eliminate_start
def findmedian(eliminate_start,eliminate_end,start1,end1,start2,end2):
    if eliminate_start==0:
        return start1,start2,end1,end2
    elif Array1[start1]<Array2[start2]:
        start1+=1
        eliminate_start-=1
    elif Array1[start1]>Array2[start2]:
        start2+=1
        eliminate_start-=1

    if Array1[end1]<Array2[end2]:
        end2-=1
        eliminate_end-=1
    else:
        end1-=1
        eliminate_end-=1
    return findmedian(eliminate_start,eliminate_end,start1,end1,start2,end2)

median=findmedian(eliminate_start,eliminate_end,0,len(Array1)-1,0,len(Array2)-1)
start1=median[0]
start2=median[1]
end1=median[2]
end2=median[3]
print(start1,start2,end1,end2)
if start1==end2 and start2==end1:
    if Array1[start1]<Array2[start2]:
        print((Array1[start1]+Array1[end1])/2)
    else:
        print((Array2[start2]+Array2[end2])/2)
elif start1==end1 and start2==end2:
    print((Array1[start1]+Array2[start2])/2)
elif start1==end1:
    print(Array1[start1])
elif start2==end2:
    print(Array2[start2])
