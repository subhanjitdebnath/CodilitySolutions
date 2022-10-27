#In the give array of num find the missing smallest positive num
#Complecity is O(n) and space complexity is constant

def solution(a):
    l=len(a)
    i=0
    while(i<l):
        ci=a[i]-1
        if(a[i]>0 and ci<l and a[i]!=i+1):
            a[i],a[ci]=a[ci],a[i]
        else:
            i+=1
        print(str(a))
    i=0
    while(i<l):
        if(a[i]!=i+1):
            return i+1
        else:
            i+=1
    return l+1

Arr=[2,1,3]
print(str(solution(Arr)))
    