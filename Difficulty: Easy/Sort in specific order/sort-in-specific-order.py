#User function Template for python3

class Solution:
    def sortIt(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
        even=[]
        odd=[]
        for i in range(n):
            if(arr[i]%2==0):
                even.append(arr[i])
            else:
                odd.append(arr[i])
        odd.sort(reverse=True)
        arr.clear()
        for i in range(len(odd)):
            arr.append(odd[i])
        for i in range(len(even)):
            arr.append(even[i])
            
        
        # a.extend(b)
        
        # return arr
        
    






#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(arr)
        print(*arr)
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends