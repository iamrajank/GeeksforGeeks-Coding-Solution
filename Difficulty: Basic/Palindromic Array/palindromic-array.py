def isPalinArray(arr):
    # iterating over each element in the array
    for i in arr:
        # checking if the string representation of the element
        # is not equal to its reverse, if so return False
        if str(i)!=str(i)[::-1]:
            return False
    # if all elements pass the condition, return True
    return True





#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if isPalinArray(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends