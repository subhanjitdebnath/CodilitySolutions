def BubbleSort(a):
    l=len(a)
    check=True
    count=0
    while(check):
        check=False
        for j in range(1,l):
            if(a[j-1]>a[j]):
                check=True
                a[j],a[j-1]=a[j-1],a[j]
            count+=1   
    print(f"\n Bubble sort takes {count} counts")
    return a

Arr=[56,55,89,42,46,32,28,25,21,10,98,56,63]
print("\n Before Sorting \n" + str(Arr))
Arr=BubbleSort(Arr)
print("\n After Sorting \n"+ str(Arr))

