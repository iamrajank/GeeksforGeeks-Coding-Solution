#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        # Sum = 0
        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         Sum = Sum + arr[i] ^ arr[j]
        # return Sum
        
        sum = 0
        for i in range(0, 32):
 
        #  Count of zeros and ones
            zc = 0
            oc = 0
          
        # Individual sum at each bit position
            idsum = 0
            for j in range(0, n):
                if (arr[j] % 2 == 0):
                    zc = zc + 1
                 
                else:
                    oc = oc + 1
                arr[j] = int(arr[j] / 2)
         
          
        # calculating individual bit sum 
            idsum = oc * zc * (1 << i)
  
        # final sum    
            sum = sum + idsum; 
     
        return sum
    






#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


    print("~")
# } Driver Code Ends