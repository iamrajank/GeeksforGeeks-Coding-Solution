class Solution:
    def reverseArray(self, arr):
        # code here
        i = 0
        j = len(arr)-1
        while i < j:
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr
            
        
        
        