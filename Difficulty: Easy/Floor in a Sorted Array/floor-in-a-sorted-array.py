class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        l = 0
        r = len(arr) - 1
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] <= x:
                l = mid + 1
                ans = mid
            else: 
                r = mid - 1
        return ans
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends