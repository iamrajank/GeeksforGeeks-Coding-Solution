#User function Template for python3

class Solution:
    def longestSubarray(self, a, n) : 
        #Complete the function
        #Brute Force Approach
        
        # temp = []
        # count = 0
        # for i in range(len(a)):
        #     for j in range(i,len(a)+1):
        #         s = 0
        #         for l in range(i,j):
        #             s = s + a[l]
        #         if s == k:
        #             count = max(count,j-i)
        # return count
        
        x={}
        currsum=0
        maxlen=0
        for i in range(len(arr)):
            currsum+=arr[i]
            if currsum==k:
                maxlen=i+1
            if (currsum-k) in x:
                maxlen=max(maxlen,i-x[currsum-k])
            if currsum not in x:
                x[currsum]=i
        return maxlen
        
    









#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends