class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        f_large = arr[0]
        s_large = -1
        for i in range(1,len(arr)):
            if arr[i] > f_large:
                s_large = f_large
                f_large = arr[i]
                
            elif arr[i] < f_large and arr[i] > s_large:
                s_large = arr[i]
        return s_large

                
        