#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        # Better approach
        
        # f_largest = arr[0]
        # for i in range(1,len(arr)):
        #     if arr[i] > f_largest:
        #         f_largest = arr[i]
                
        # s_largest = -1
        # for i in range(len(arr)):
        #     if arr[i] > s_largest and arr[i] != f_largest:
        #         s_largest = arr[i]
        # return s_largest
        
        # Optimal aproach
        
        flargest = arr[0]
        slargest = -1
        for i in range(1,len(arr)):
            if arr[i] > flargest:
                slargest = flargest
                flargest = arr[i]
            elif arr[i] < flargest and arr[i] > slargest:
                slargest = arr[i]
        return slargest
        














#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends