#In the array of number from 1to n , one of the number is dublicated and this has resulted in lost of another number
#Task is to find the dublicated number and find the missing number

def Solution(a):
    l=len(a)
    i=0
    a1=[]
    while(i<l):
        if(a[i]!=i+1):
            ci=a[i]-1
            if(a[i]!=a[ci]):
                a[i],a[ci]=a[ci],a[i]
            else:
                i+=1
        else:
            i+=1
    i=0
    while(i<l):
        if(a[i]!=i+1):
            a1.append(a[i])
            a1.append(i+1)
            return a1
        else:
            i+=1
    return -1


Arr=[1,1]
print("\n"+str(Solution(Arr)))


