#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        i = 0
        j = i + 1
        n = len(arr)
        ans = 0
        maxi = -1000000
        while j < n:
            ans = arr[i] + arr[j]
            maxi = max(ans,maxi)
            i = i + 1
            j = j + 1
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends