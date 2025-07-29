import math
class Solution:
    def gcd(self, a, b):
        # code here
        # if a > b:
        #     small = b
        # else:
        #     small = a
        
        # for i in range(1,small+1):
        #     if a % i == 0 and b % i == 0:
        #         gcd = i
        # return gcd
        
        if b == 0:
            return a
        else:
            return math.gcd(b,a%b)
            