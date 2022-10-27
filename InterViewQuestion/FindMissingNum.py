#There are 0 to n number in array find the missing number. 
def FindmissingNum(a,l):
    sum=int((l*(l+1))/2)
    sum2=0
    for i in a:
        sum2+=i
    return sum-sum2

def FindMissNum(a,l):
    l1=len(a)
    i=0
    while(i<l1):
        ci=a[i]
        if(ci<l1 and a[i]==a[ci]):
            a[i],a[ci]=a[ci],a[i]
        else:
            i+=1
    i=0
    while(i<l1):
        if(a[i]!=i):
            return i
        else:
            i+=1
    return l

def MissnumNotInList(a):
    l=len(a)
    i=0
    a1=[]
    while(i<l):
        ci=a[i]-1
        if(a[i]!=a[ci]):
            a[i],a[ci]=a[ci],a[i]
        else:
            i+=1
    i=0
    print(str(a))
    while(i<l):
        if(a[i]!=i+1):
            a1.append(i+1)
        i+=1
    return a1


Arr=[4,3,2,7,8,2,3,1]
n=5
print(f"\n Missing number is {MissnumNotInList(Arr)}")
