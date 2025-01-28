#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        # code here
        
        # Brute Force Approach
        
        # result = 0    
        # for i in range(len(arr)):
        #     ans = 0
            
        #     for j in range(i,len(arr)):
        #         ans = ans + arr[j]
            
        #         if ans == 0:
        #             result = max(result,j-i+1)
        # return result
        
        x={}
        currsum=0
        maxlen=0
        for i in range(len(arr)):
            currsum+=arr[i]
            if currsum==0:
                maxlen=i+1
            if (currsum-0) in x:
                maxlen=max(maxlen,i-x[currsum-0])
            if currsum not in x:
                x[currsum]=i
        return maxlen
                
                
                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends