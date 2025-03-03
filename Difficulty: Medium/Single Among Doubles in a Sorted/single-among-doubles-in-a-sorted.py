#User function Template for python3

class Solution:
    def findOnce(self,nums):
        # Complete this function
          # method 1 (using hashing)
        # temp = {}
        # for i in nums:
        #     if i not in temp:
        #         temp[i] = 1
        #     else:
        #         temp[i] += 1
        # for i in temp:
        #     if temp[i] == 1:
        #         return i

        # method - 2 (using xor operation)
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        # n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr))
        print("~")

# } Driver Code Ends