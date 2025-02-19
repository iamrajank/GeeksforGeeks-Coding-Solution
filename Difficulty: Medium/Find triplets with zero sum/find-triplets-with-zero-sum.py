#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr):
        #code here
        arr.sort()
        for i in range(len(arr)):
            l = i + 1
            r = len(arr) - 1
            while l < r:
                result = arr[i] + arr[l] + arr[r]
                if result == 0:
                    return True
                elif result < 0:
                    l = l + 1
                else:
                    r = r - 1
        return False
  
        





#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    n = len(arr)  # get the length of the array
    if Solution().findTriplets(arr):
        print("true")
    else:
        print("false")

# } Driver Code Ends