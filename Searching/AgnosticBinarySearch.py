#Here we need to detect if the array is sorted in assending or decending order
#Then we need to apply the Binary search algorith

def AgonisticBinarySearch(a,target):
    l=len(a)
    Start=0
    End=l-1
    IsAsnd=(a[Start]<a[End])
    ISEqual=(a[Start]==a[End])
    while(Start<=End):
        mid=int(Start+(End-Start)/2)
        if(a[mid]==target):
            return mid # found
        else:
            if(IsAsnd): # For Assending
                if(a[mid]<target):
                    Start=mid+1
                else:
                    End=mid-1
            else: # For Decending
                if(a[mid]>target):
                    Start=mid+1
                else:
                    End=mid-1
    return -1

#Arr=[5,9,12,26,28,32,34,36,39,45,48,52,54]
Arr=[89,78,69,54,51,49,47,42,21,15,14,9,8,7,7,2]

target=int(input("Enter the value to be search \n"))
print(f"\n {target} is present at index {AgonisticBinarySearch(Arr,target)}")



