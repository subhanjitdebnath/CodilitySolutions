def InserstionSort(a):
    l=len(a)
    j=0
    count=0

    for i in range(l-1):
        j=i+1
        while(j>0):
            count+=1
            if(a[j-1]>a[j]):
                a[j-1],a[j]=a[j],a[j-1]
            else:
                break
            j-=1
            
    print(f"\n Insertion sort takes {count} counts")
    return a

Arr=[56,55,89,42,46,32,28,25,21,10,98,56,63]
print("\n Before Sorting \n" + str(Arr))
Arr=InserstionSort(Arr)
print("\n After Sorting \n"+ str(Arr))