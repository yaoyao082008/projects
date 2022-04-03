Array1=[1,2,2,4]
Array2=[1,4,4,5]
start1=0
end1=len(Array1)-1
sp1=0
sp2=0
median1=0
median2=0
while  True:
    sp1=(start1+end1)//2
    sp2=len(Array1)-(sp1)-1
    if (Array1[sp1]>=Array2[sp2-1] and Array2[sp2]>=Array1[sp1-1] 
    or sp2==0 and Array2[sp2]>=Array1[sp1-1] 
    or sp1==0 and Array1[sp1]>=Array2[sp2-1]):
        break
    if Array1[sp1]<Array2[sp2]:
        start1=sp1+1
    else:
        end1=sp1
print(sp1,sp2)
median1=Array1[sp1]
median2=Array2[sp2]
if sp1+1<len(Array1) and Array1[sp1+1]<Array2[sp2]:
    median1=Array1[sp1]
    median2=Array1[sp1+1]
elif sp2+1<len(Array1) and Array2[sp2+1]<Array1[sp1]:
    median1=Array2[sp2]
    median2=Array2[sp2+1]
print((median1+median2)/2)

