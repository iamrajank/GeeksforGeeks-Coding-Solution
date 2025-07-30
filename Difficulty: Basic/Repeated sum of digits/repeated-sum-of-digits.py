#User function Template for python3
class Solution:
    def repeatedSumOfDigits (self,N):
        # code here 
        while N >= 10:
            result = 0
            while N > 0:
                digit = N % 10
                result = result + digit
                N = N // 10
            N = result
        return N