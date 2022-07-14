


def dial(n):
    #x={1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],6:[1,0,7],7:[6,2],8:[1,3],9:[4,2],0:[4,6]}
    arr1=[1,0]
    arr2=[0,0]
    arr3=[0,0]
    arr4=[0,0]
    arr6=[0,0]
    arr7=[0,0]
    arr8=[0,0]
    arr9=[0,0]
    arr10=[0,0]
    count=0
    for i in range(n):
        arr1[-1]=(arr6[0]+arr8[0])
        arr2[-1]=(arr7[0]+arr9[0])
        arr3[-1]=(arr4[0]+arr8[0])
        arr4[-1]=(arr3[0]+arr9[0]+arr10[0])
        arr6[-1]=(arr1[0]+arr7[0]+arr10[0])
        arr7[-1]=(arr6[0]+arr2[0])
        arr8[-1]=(arr1[0]+arr3[0])
        arr9[-1]=(arr4[0]+arr2[0])
        arr10[-1]=(arr4[0]+arr6[0])
        arr1[0]=arr1[-1]
        arr2[0]=arr2[-1]
        arr3[0]=arr3[-1]
        arr4[0]=arr4[-1]
        arr6[0]=arr6[-1]
        arr7[0]=arr7[-1]
        arr8[0]=arr8[-1]
        arr9[0]=arr9[-1]
        arr10[0]=arr10[-1]


    count+=arr1[-1]
    count+=arr2[-1]
    count+=arr3[-1]
    count+=arr4[-1]
    count+=arr6[-1]
    count+=arr7[-1]
    count+=arr8[-1]
    count+=arr9[-1]
    count+=arr10[-1]
        
    return count


print(dial(7))

