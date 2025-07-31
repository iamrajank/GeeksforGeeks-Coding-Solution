#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] +=1
        for i,j in temp.items():
            if j == 1:
                return i

