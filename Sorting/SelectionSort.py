def SelectionSort(a):
    l=len(a)
    max=0
    k=0
    count=0
    for i in range(l):
        max=a[0]
        k=0
        for j in range(1,l-i):
            if(max<a[j]):
                k=j
                max=a[j]
            count+=1
        a[l-i-1],a[k]=max,a[l-i-1]
    print(f"\n Selection sort takes {count} counts")
    return a

Arr=[56,55,89,42,46,32,28,25,21,10,98,56,63]
print("\n Before Sorting \n" + str(Arr))
Arr=SelectionSort(Arr)
print("\n After Sorting \n"+ str(Arr))


