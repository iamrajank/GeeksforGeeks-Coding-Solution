class Solution:
    def maxSubArraySum(self, nums):
        # Your code here
        s=0
        res=nums[0]
        for i in range(len(nums)):
            s+=nums[i]
            if s>res:
                res=s
            if s<0:
                s=0
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends