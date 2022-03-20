#Array0=[4,5,7,10]
#Array1=[1,3,8,9]
Array0=[1,2,3,4]
Array1=[5,6,7,8]
elimnate=len(Array0)-1
start0=0
end0=len(Array0)-1
start1=0
end1=len(Array1)-1
sp0=0
sp1=1
median=0
median1=0
while elimnate>1:
    sp0=(start0+end0)//2
    sp1=(start1+end1)//2
    if Array0[sp0]<Array1[sp1]:
        elimnate=elimnate-(sp0-start0)
        start0=sp0
    if Array1[sp1]<Array0[sp0]:
        elimnate=elimnate-(sp1-start1)
        start1=sp1
if Array0[sp0]<Array1[sp1]:
    median=Array0[start0+1]
    median1=Array1[start1-1]


print((median+median1)//2)



