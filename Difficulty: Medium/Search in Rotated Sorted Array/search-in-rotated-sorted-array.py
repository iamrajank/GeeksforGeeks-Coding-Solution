#User function Template for python3

class Solution:
    def search(self, num : list, target : int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        
        # we can also solve using linear search but it takes O(N). That's wht we can use Binary search
        
        l = 0
        r = len(num)-1
        while l <= r:
            mid = l + (r-l)//2
            if num[mid] == target:
                return mid
    
            elif num[l] <= num[mid]:
                if num[l] <= target and target <= num[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if num[mid] <= target and target <= num[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        
        
        # while l <= h:
        #     mid = (l + h) // 2

        #     # Check if key is present at mid
        #     if A[mid] == key:
        #         return mid

        #     # If the left half is sorted
        #     if A[l] <= A[mid]:
        #         # Check if key is present in the left half
        #         if A[l] <= key <= A[mid]:
        #             h = mid - 1
        #         else:
        #             l = mid + 1
        #     # If the right half is sorted
        #     else:
        #         # Check if key is present in the right half
        #         if A[mid] <= key <= A[h]:
        #             l = mid + 1
        #         else:
        #             h = mid - 1

        # # If key is not present in the array
        # return -1
                
       
                    
     
                
                
                
                

    
        
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends