#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        if x == 0:
            return 0
        first = 1
        last = x
        while first <= last:
            mid = first + (last-first)//2
            result = x // mid
            if result == mid:
                return mid
            elif result < mid:
                last = mid - 1
            elif result > mid:
                first = mid + 1
        return last
   





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends