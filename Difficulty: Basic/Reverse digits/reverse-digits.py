#User function Template for python3

class Solution:
	def reverseDigits(self, x):
		# Code here
        result = 0
   
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10
        return result