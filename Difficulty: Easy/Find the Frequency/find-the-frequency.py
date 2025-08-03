"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i,j in temp.items():
            if i == x:
                return j
        return 0