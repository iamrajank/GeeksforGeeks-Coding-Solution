#User function template for Python

class Solution:    
    def removeDuplicates(self, A):
        # code here
        # j = 1
        # i = 0
        # while j < len(A):
        #     if len(A) == 1:
        #         return len(A)
        #     elif A[i] == A[j]:
        #         A.remove(A[i])
        #     else:
        #         i = i + 1
        #         j = j + 1
        # return len(A)
        
        # i = 0
        # j = 1
        # while j < len(A):
        #     if A[i] == A[j]:
        #         A.remove(A[j])
        #     elif A[i]<A[j]:
        #         i = i + 1
        #         j = j + 1
        # return len(A)
        
        if len(A) == 0:
            return 0

        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
    
        return i + 1

                
    







#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends