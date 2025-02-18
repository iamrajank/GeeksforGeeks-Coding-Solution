
#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        Sum = 0
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            else:
                Sum = Sum + num
                num = 0
        result = Sum + num
        return result
                
                
       





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.findSum(s))
        print("~")

# } Driver Code Ends