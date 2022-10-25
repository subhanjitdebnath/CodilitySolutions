class SortLib():
    def __init__(self):
        pass
    def BubbleSort(self,a):
        l=len(a)
        count=0
        check=True
        while(check):
            check=False
            for j in range(1,l):
                if(a[j-1]>a[j]):
                    check=True
                    a[j],a[j-1]=a[j-1],a[j]
                count+=1
        
        print(f"\n Bubble sort takes {count} counts")
        return a
    def SelectionSort(self,a):
        l=len(a)
        max=0
        count=0
        k=0
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
    
    def InserstionSort(self,a1):
        l=len(a1)
        j=0
        counts=0
        for i in range(l-1):
            j=i+1
            while(j>0):
                counts+=1
                if(a1[j-1]>a1[j]):
                    a1[j-1],a1[j]=a1[j],a1[j-1]
                else:
                    break
                j-=1
                
                
        print(f"\n Insertion sort takes {counts} counts")
        return a1

if "__main__"==__name__:
    Arr=[56,55,89,42,46,32,28,25,21,10,98,56,63]
    print("\n Before Sorting \n" + str(Arr))
    a1=[]
    a2=[]
    a3=[]
    srt=SortLib()
    # a1=srt.BubbleSort(Arr)
    # print("\n After Bubble sort \n"+ str(a1))
    a3=srt.SelectionSort(Arr)
    print("\n After Selection sort \n"+ str(a3))
    a2=srt.InserstionSort(Arr)
    print("\n After Insertion sort \n"+ str(a2))
    
    
    

