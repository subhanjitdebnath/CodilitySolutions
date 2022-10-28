SortedList=[12,15,23,45,58,98,144,214,245,289]

def BinarySearch(List,Targ,start=0,end=0):
    while(start<=end):
        mid=int(start+(end-start)/2)
        if(List[mid]==Targ):
            return mid
        else:
            if(List[mid]<Targ):
                start=mid+1
            else:
                end=mid-1
    return -1    
print("Enter the value to be search ")
target=int(input())
ans=BinarySearch(SortedList,target,0,len(SortedList)-1)
print(str(ans))





