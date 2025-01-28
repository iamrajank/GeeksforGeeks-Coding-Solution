#User function template for Python 3

class Solution:
    def majorityElement(self, A):
        #Your code here
        
        # for i in range(len(A)):
        #     result = N//2
        #     if A.count(A[i]) > result:
        #         return A[i]
        # return -1
        
        N = len(A)
        if N==1:
            return A[0]
        dic = {}
        for i in A:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
            if dic[i]>(N//2):
                return i
                break
        return -1








#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends