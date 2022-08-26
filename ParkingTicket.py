def solution(E, L):
    # write your code in Python 3.6
    EntryTime=[]
    LeaveTime=[]
    EntryTime=list(map(lambda x:int(x) ,E.split(":")))
    LeaveTime=list(map(lambda x:int(x) ,L.split(":")))
    #print(EntryTime)
    #print(LeaveTime)
    hours=LeaveTime[0]-EntryTime[0]
    mint=LeaveTime[1]-EntryTime[1]
    if(mint!=0):
        if(mint<0):
           return (5 + 4*(hours -1))
        else:
             return (5 + 4*hours)
    else:
        return (5+4*(hours-1))