#User function Template for python3

class Solution:
    def isPerfectNumber(self, n):
        # code here 
        count = 0
        for i in range(1,int(n**0.5)+1):
            if n % i == 0:
                temp = int(n/i)
                if temp != n:
                    count = count + i + temp
                else:
                    count = count + i
        if count == n:
            return True
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = (ob.isPerfectNumber(N))
        if (ans):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends