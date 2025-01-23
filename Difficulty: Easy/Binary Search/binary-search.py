#User function template for Python

class Solution:    
    def binarysearch(self, arr, n):
        # code here
        s,e=0,len(arr)-1
        while s<=e:
            m=s+(e-s)//2
            if arr[m]<k:
                s=m+1
            elif arr[m]==k:
                if m==0 or arr[m-1]!=k:
                    return m
                e=m-1
            else:
                e=m-1
        return -1





#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends