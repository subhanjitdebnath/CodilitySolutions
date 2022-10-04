class ChoclateByNum:
    def __init__(self):
        pass
    def TotalChoclate(self,N,M):
        """N=Total Number of choclate M=Steps to eat"""
        count=0
        i=0
        Cholate=[]
        while(True):
            if(i in Cholate) or (N<M):
                break
            else:
                Cholate.append(i)
                count+=1
            i=i+M
            if(i>=N):
                i=(i-N)
        print(str(count))

if __name__ == "__main__":
    a=ChoclateByNum()
    a.TotalChoclate(1,2)
            