#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    
    def get_min_max( a, n):
        small = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < small:
                small = arr[i]
        large = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > large:
                large = arr[i]
        return small,large

    
    
    




#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")


# } Driver Code Ends