def Finddublicate(a):
    l=len(a)
    i=0
    a1=[]
    while(i<l):
        ci=a[i]-1
        if(ci!=i):
            if(a[ci]==a[i]):
                i+=1
            else:
                a[ci],a[i]=a[i],a[ci]
        else:
            i+=1
    i=0
    while(i<l):
        if(a[i]!=i+1):
            a1.append(a[i])
        i+=1
    return a1
def Finddublicate1(a):
    l=len(a)
    i=0
    a1=[]
    while(i<l):
        if(a[i]!=i+1):
            ci=a[i]-1
            if(a[ci]!=a[i]):
                a[i],a[ci]=a[ci],a[i]
            else:
                a1.append(a[i])
                i+=1
        else:
            i+=1
    return a1


Arr=[4,3,2,7,8,2,3,1]
print(str(Finddublicate(Arr)))
