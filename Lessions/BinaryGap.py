#Enter the decimal number and the code will return the max binay gap between the 1's.
#Conversion of decimal to bainary is done and the gap is found

def MaxbinaryGap(num):
    flag=False
    Maxgap=0
    gap=0
    while(num!=0):
        rem=num%2
        if(rem==1 and not flag):
            flag=True
        elif(flag and rem==0):
            gap+=1
        elif(flag and rem==1):
            if(Maxgap<gap):
                Maxgap=gap
                gap=0
            else:
                gap=0
        num=num//2
    return Maxgap

if __name__=="__main__":
    num= int(input("Enter the number  "))
    print(f"The Max gap in the number {num} is {MaxbinaryGap(num)} ")

