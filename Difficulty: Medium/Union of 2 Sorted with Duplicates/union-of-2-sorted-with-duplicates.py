#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2):
        # code here 
        
        # Brute force
        
        temp = set()
        for i in a:
            temp.add(i)
        for i in b:
            temp.add(i)
        result = list(temp)
        result.sort()
        return result
        
        # Two pointer
        
        # i = 0
        # j = 0
        # n = len(a)
        # m = len(b)
        # temp = []
        
        # while i < n and j < m:
        #     if a[i] == b[j]:
        #         temp.append(a[i])
        #         i += 1
        #         j += 1
        #     elif a[i] < b[j]:
        #         temp.append(a[i])
        #         i += 1
        #     elif a[i] > b[j]:
        #         temp.append(b[j])
        #         j += 1
        # # insert the remaining element
        # for i in a:
        #     if i not in temp:
        #         temp.append(i)
        # for i in b:
        #     if i not in temp:
        #         temp.append(i)
        # result = []
        # for i in temp:
        #     if i not in result:
        #         result.append(i)
        # return result
        
        i, j = 0, 0  # Pointers
        union = []  # Union list

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:  # Case 1 and 2
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                    i += 1
                else:  # Case 3
                    if len(union) == 0 or union[-1] != arr2[j]:
                        union.append(arr2[j])
                        j += 1

        while i < len(arr1):  # If any elements left in arr1
            if union[-1] != arr1[i]:
                union.append(arr1[i])
                i += 1

        while j < len(arr2):  # If any elements left in arr2
            if union[-1] != arr2[j]:
                union.append(arr2[j])
                j += 1

        return union
    
        
        
            
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends