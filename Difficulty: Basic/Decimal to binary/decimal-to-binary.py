#User function Template for python3
def toBinary(n):
    result = ""
    while n > 0:
        temp = n % 2
        result = result + str(temp)
        n = n // 2
    print(result[::-1])






#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    for _ in range(int(input())):
        n=int(input())
        toBinary(n)

    
# } Driver Code Ends