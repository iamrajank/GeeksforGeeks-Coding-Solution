class Solution:
    def leaders(self, arr):
        # code here
        
        # # //Brute Force
        # ans = []
        # for i in range(len(arr)):
        #     leader = True
        #     for j in range(i+1,len(arr)):
        #         if arr[j] > arr[i]:
        #             leader = False
        #             break
        #     if leader:
        #         ans.append(arr[i])
        # return ans
            
        
        # Optimal Solution
        ans = []
        n = len(arr)
        max_ele = arr[n-1]
        ans.append(max_ele)
        for i in range(n-2,-1,-1):
            if arr[i] >= max_ele:
                ans.append(arr[i])
                max_ele = arr[i]
        return ans[::-1]
        
     

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends