#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        ans = 0
        for i in str(n):
            if int(i) == 0:
                continue
            elif n % int(i) == 0:
                ans = ans + 1
        return ans