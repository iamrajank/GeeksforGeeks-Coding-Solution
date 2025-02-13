#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def findMatching(self, haystack, needle):
        # Code here
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        text, pattern = input().split()
        ob = Solution()
        res = ob.findMatching(text, pattern)
        print(res)
        print("~")
# } Driver Code Ends