class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        l, r = 0, len(arr)-1
        res = []
        arr.sort()
        
        for i in range(len(arr)):
            if i%2==0:
                res.append(arr[r])
                r-=1
            else:
                res.append(arr[l])
                l+=1
                
        return res





#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends