#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        pass
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist):
        #code here
       
        for i in range(1,len(alist)):
            key = alist[i]
            j = i - 1
            while j >= 0 and alist[j] > key:
                alist[j+1] = alist[j]
                j = j - 1
            alist[j+1] = key
        return alist
            
        







#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.insertionSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends