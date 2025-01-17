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
    def insertionSort(self, arr):
        #code here
        for i in range(1,len(arr)):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key
        return arr
       






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