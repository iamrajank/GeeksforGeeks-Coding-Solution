#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] +=1
        for i,j in temp.items():
            if j == 1:
                return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
        print("~")
# } Driver Code Ends