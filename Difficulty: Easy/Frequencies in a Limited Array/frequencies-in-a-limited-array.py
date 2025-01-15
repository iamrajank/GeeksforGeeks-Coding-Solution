class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
                
        temp = {}
        for i in arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        tem = []
        N= len(arr)
        for i in range(1,N+1):
            if i not in temp:
                tem.append(0)
            else:
                tem.append(temp[i])
        arr.clear()
        for i in tem:
            arr.append(i)
        return arr
        
                
            
        
        




#{ 
 # Driver Code Starts
# Main code to read input and process each test case
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().frequencyCount(arr)  # find the frequencies

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print the result
    else:
        print("[]")  # Print empty list if no valid frequencies

# } Driver Code Ends