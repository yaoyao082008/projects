

Array=[2,4,6,9,10,12]
Array1=[11,15,18,23,56,89]
#Median= (Array[len(Array)//2] + Array[len(Array)-1])/2
#Median1= (Array1[len(Array1)//2] + Array1[len(Array1)-1])/2
#if the spliting point of one array is larger than the other then i remove the larger ones and vice versa
numberstoeliminate=len(Array)-1
splittingPoint=0
splittingPoint1=0
starting=0
ending=len(Array)
while numberstoeliminate>0:
        splittingPoint= (starting+ending)//2
        if Array[splittingPoint]>Array1[splittingPoint]:
            ending=splittingPoint
            numberstoeliminate=ending
        if Array[splittingPoint]<Array1[splittingPoint]:
            starting=splittingPoint
            numberstoeliminate=numberstoeliminate-starting
print(Array[splittingPoint])
print(Array1[len(Array1)-1-numberstoeliminate])
print((Array[splittingPoint]+Array1[len(Array1)-1-splittingPoint])/2)
        

