#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, nums, k):
        #Your code here
        n = len(nums)
        i = 0
        k = k % n
        j = k-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        i = k
        j = n - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        i = 0
        j = n - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        return nums


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends