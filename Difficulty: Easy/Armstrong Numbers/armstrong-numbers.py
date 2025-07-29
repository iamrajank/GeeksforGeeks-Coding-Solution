#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        result = 0
        power = len(str(n))
        n_copy = n
        while n > 0:
            digit = n % 10
            result = result + digit ** power
            n = n // 10
        if n_copy == result:
            return True
        else:
            return False
        