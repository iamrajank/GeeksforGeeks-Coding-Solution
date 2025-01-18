#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == k:
                return True
            elif arr[mid] > k:
                r = mid - 1
            elif arr[mid] < k:
                l = mid + 1
                
        return False
        
        # l = 0
        # r = len(arr) - 1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if arr[mid] == K:
        #         return 1
        #     elif arr[mid] > K:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends