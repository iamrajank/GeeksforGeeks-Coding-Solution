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








