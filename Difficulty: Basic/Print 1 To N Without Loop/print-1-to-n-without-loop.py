#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        for i in range(1,n+1):
            print(i, end = " ")
            
        # if N == 0:
        #     return
        # else:
            
        #     self.printNos(N-1)
        #     print(N, end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends