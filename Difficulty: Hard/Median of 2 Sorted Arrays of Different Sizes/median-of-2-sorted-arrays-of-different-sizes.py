#User function Template for python3

class Solution:
    def medianOf2(self, array1, array2):
            #code here
        arr1=array1+array2
        arr1.sort()
        n=len(arr1)
        if n%2==0:
            median=(arr1[n//2-1]+arr1[n//2])/2
            median = int(median) if median.is_integer() else median
        else:
            median=arr1[n//2]
        return median








#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")

# } Driver Code Ends