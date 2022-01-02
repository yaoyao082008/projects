Array=[1,2,4,5,7,11,100,113,200,250]
search1=input("Please type in a integer you want to search for: ")
search=int(search1)
find=len(Array)//2
def Search(starting,ending,find):
    if ending-starting>=1:
        if Array[find]<search:
            starting=find
            find =(starting+ending)//2
            return Search(starting+1,ending,find)
        if Array[find]>search:
            ending=find
            find=find//2
            return Search(starting,ending,find)
        else:
            return find
    else:
        if Array[ending]==search:
            return ending
        elif Array[starting]==search:
            return starting
        else:
            return -1
k=Search(0,len(Array)-1,find)
if Array[k]==search:
    print("Value Found! Index %s"%k)
else:
    print("Value Not Found. Please make sure you have typed in the right value")
