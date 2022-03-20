Array1=[1,2,3,4,5]
Array2=[6,7,8,9,10]
eliminate_start= (len(Array1)+len(Array2)-1)//2
eliminate_end= eliminate_start
start1=0
start2=0
end1=len(Array1)-1
end2=len(Array2)-1

while eliminate_start!=0 and eliminate_end!=0:
    if Array1[start1]<Array2[start2]:
        start1+=1
        eliminate_start-=1
    else:
        start2+=1
        eliminate_start-=1

    if Array1[end1]<Array2[end2]:
        end2-=1
        eliminate_end-=1
    else:
        end1-=1
        eliminate_end-=1
print(start1,end1,start2,end2)
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

