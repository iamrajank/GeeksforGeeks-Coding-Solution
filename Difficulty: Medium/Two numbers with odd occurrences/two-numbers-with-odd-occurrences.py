#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        temp = {}
        for i in Arr:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        a = []
        for i,j in temp.items():
            if j % 2 != 0:
                a.append(i)
        a.sort(reverse = True)  
        return a



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
        print("~")
# } Driver Code Ends