#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,nums):
		# code here
		# Better approach
        
        # result = nums[0]
        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(i,len(nums)):
        #         ans = ans * nums[j]
        #         result = max(result,ans)
        # return result

        # Optimal

        n = len(nums) # size of array.

        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends