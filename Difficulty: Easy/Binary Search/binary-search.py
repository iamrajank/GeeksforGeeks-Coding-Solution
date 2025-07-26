class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        n = len(arr)
        l = 0
        r = n - 1
        result = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == k:
                result = mid
                r = mid - 1
            elif arr[mid] > k:
                r = mid - 1
            else:
                l = mid + 1
        return result
        
        