#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
        #code here 
    #     temp = []
    #     for i in range(1,N+1):
    #         if N % i == 0:
    #             temp.append(i)
    #     ans = 0
    #     for i in temp:
    #         ans = ans + i
    #     return ans
    
        total_sum = 0
        for i in range(1, N + 1):
            total_sum += (N // i) * i
        return total_sum





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
        print("~")

# } Driver Code Ends