#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        #code here
        
        # Brute Force Approach (TLE Error)
        
        # temp = []
        # fact = 1
        # for i in range(1,n+1):
        #     fact = fact * i
        #     if fact < n:
        #         temp.append(fact)
        # return temp
        
        temp = []
        fact = 1
        i = 1
        while fact <= n:
            temp.append(fact)
            i = i + 1
            fact = fact * i
            
            
        return temp
            
            
    






#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends