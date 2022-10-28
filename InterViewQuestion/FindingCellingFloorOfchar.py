#For a given character we need to find next larger character in the array
#The letter also wrap arround

def Solution(a,target):
    l=len(a)
    start=0
    end=l-1
    if(a[end]<=target):
        return a[start]
    while(start<=end):
        mid=int(start+(end-start)/2)
        if(a[mid]==target):
            return a[mid+1]
        else:
            if(a[mid]<target):
                start=mid+1
            else:
                end=mid-1
    return a[start]

#Better solution for the same thing
def Solution1(a,target):
    l=len(a)
    start=0
    end=l-1
    while(start<=end):
        mid=int(start+(end-start)/2)
        if(a[mid]<=target):
            start=mid+1
        else:
            end=mid-1
    return a[start%l]

Arr=['c','f','n','q','s','u','w']
target = input("Enter the char need to find ")
print(f"\n The next greater char after {target} is {Solution1(Arr,target)}")