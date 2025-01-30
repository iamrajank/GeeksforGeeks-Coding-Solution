#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        # temp = []
        # for i in range(len(arr)):
        #     if arr.count(arr[i]) > 1:
        #         temp.append(arr[i])
        # unique_temp = list(set(temp))
        
        # a = list(set(arr))
        # Sum_a = sum(a)
        # n = len(a)
        # result = (n * (n+1) // 2)
        # final = abs(result - Sum_a)
        # unique_temp.append(final)
        # return unique_temp
        
        sumarr = sum(arr)
        n = len(arr)
        exsum = (n * (n+1))/2
        
        for j in range(n):
            if (arr[abs(arr[j])-1] < 0):
                rep = abs(arr[j])
                break
            else:
                arr[abs(arr[j])-1] = arr[abs(arr[j])-1] * (-1)
                
        sumarr = sumarr - rep
        miss = int(exsum - sumarr)
        
        return [rep, miss]
  
       
   
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends