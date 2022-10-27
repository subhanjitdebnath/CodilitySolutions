def CyclicSort(a):
    l=len(a)
    i=0
    while(i<l):
        correctindex=a[i]-1
        if(a[i]!=a[correctindex]):
            a[i],a[correctindex]=a[correctindex],a[i]
        else:
            i+=1
    return 

def CyclicSort1(a):
    l=len(a)
    i=0
    while(i<l):
        correctindex=a[i]
        if(a[i]!=a[correctindex]):
            a[i],a[correctindex]=a[correctindex],a[i]
        else:
            i+=1
    return a

Arr=[9,5,8,7,4,3,1,6,2,0]
print("\n Before sorting \n"+str(Arr))
Arr=CyclicSort1(Arr)
print("\n After sorting \n"+str(Arr))
