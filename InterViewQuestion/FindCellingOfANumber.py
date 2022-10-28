#For a give number find the celling of that number from the array or the list
def FindtheCelling(a,target):
    l=len(a)
    start=0
    end=l-1
    if(target > a[end]):
        return "Not Found"
    while(start<=end):
        mid=int(start+(end-start)/2)
        if(a[mid]==target):
            return a[mid]
        elif(a[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return a[start]

#For a given number find floor of the number from the array or the list
def FindFloorNum(a,target):
    l=len(a)
    start=0
    end=l-1
    if(target < a[start]):
        return "Not Found"
    while(start<=end):
        mid=int(start +(end - start)/2)
        if(a[mid]==target):
            return target
        elif(a[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return a[end]

Arr=[2,4,5,8,12,15,19,22,28,36,38,45,49,50]
target=int(input("\n Enter the number whose celling you want to find = "))
print(f"\n The value of celling of number {target} is {FindFloorNum(Arr,target)}")
