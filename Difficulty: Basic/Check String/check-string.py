#User function Template for python3

class Solution:
    def check (self,s):
        var = s[0]
        # your code here
        for i in range(len(s)-1):
            if s[i] != var:
                return False
        return True





#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends