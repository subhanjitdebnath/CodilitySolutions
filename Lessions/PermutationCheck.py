def solution(A):
    # write your code in Python 3.6
    #check for the sum of N natural numbers
    n=len(A)
    Nsum=n*(n+1)/2
    Tsum=0
    Aset=set(A)
    for i in Aset:
        Tsum+=i
    
    if(Nsum==Tsum):
        return 1
    else:
        return 0
