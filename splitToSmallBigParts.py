array1=[3,6,1,3,2,3,0,2,4]
ifsmaller=1
value=array1[0]
back=len(array1)-1
x=len(array1)-1
        
for i in range(1,len(array1)):
    if array1[i]<value:
        array1[i],array1[ifsmaller]=array1[ifsmaller],array1[i]
        ifsmaller+=1
array1[0],array1[ifsmaller-1]=array1[ifsmaller-1],array1[0]
""" end of program"""
        

  
        

for i in range(len(array1)):
    print(array1[i])
