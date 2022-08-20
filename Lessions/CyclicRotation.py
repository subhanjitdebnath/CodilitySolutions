#Cyclic rotation of array from right to left. Shifting the elements towards right.
def solution(A, K):
    """This function will take array A and total number of shift k"""
    for i in range(K):
        temp=A[-1]
        A.pop(-1)
        A.insert(0,temp)
    return A

if __name__=="__main__":
    print(f"Shifted array {str(solution([2,3,4,8,9],4))}")