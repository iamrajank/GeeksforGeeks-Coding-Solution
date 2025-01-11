#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def lcmAndGcd(self,a , b):
        # code here 
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
    
    # Calculate GCD
        gcd_result = gcd(a, b)
    
    # Calculate LCM using the relationship between LCM and GCD
        lcm_result = (a * b) // gcd_result
    
    # Return the results as a list [LCM, GCD]
        return [lcm_result, gcd_result]
        




#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends