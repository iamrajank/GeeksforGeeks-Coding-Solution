class Solution:
    def largest(self, arr):
        # code here
        larger = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > larger:
                larger = arr[i]
        return larger
        
        
