#In the sorted array find the start and end index of the num from the list
#Ex: [2,4,7,8,8,8,9,10] find the start and end index of 8. Ans is [3,5]

def Solution(a,target):
    l=len(a)
    start=0
    end=l-1
    a1=[-1,-1]
    found=False
    count=0
    mid=0
    while(start<=end):
        count+=1
        mid=int(start +(end-start)/2)
        if(a[mid]==target):
            found=True
            break
        elif(a[mid]<target):
            start=mid+1
        else:
            end=mid-1
    if(found):
        Rev=mid
        Fwd=mid
        done=True
        while(done):
            count+=1
            done=False
            if(Rev-1>0 and a[Rev-1]==target):
                Rev-=1
                done=True
            if(Fwd+1<l and a[Fwd+1]==target):
                Fwd+=1
                done=True
        a1[0]=Rev
        a1[1]=Fwd
    print(f"\n The count is {count}")
    return a1

def BinarySearchMod(a,target,startIdx):
    l=len(a)
    start=0
    end=l-1
    idx=-1
    count=0
    while(start<=end):
        count+=1
        mid=int(start+(end-start)/2)
        if(a[mid]==target):
            idx=mid
            if(startIdx):
                end=mid-1
            else:
                start=mid+1
        elif(a[mid]<target):
            start=mid+1
        else:
            end=mid-1
    return (idx,count)

def Solution2(a,target):
    ans=[-1,-1]
    count1=0
    count2=0
    ans[0],count1=BinarySearchMod(a,target,True)
    ans[1],count2=BinarySearchMod(a,target,False)
    print(f"\n Total count{str(count1+count2)}")
    return ans


Arr=[2,4,7,7,8,8,8,8,10]
print(str(Solution(Arr,7)))

            
        
        
