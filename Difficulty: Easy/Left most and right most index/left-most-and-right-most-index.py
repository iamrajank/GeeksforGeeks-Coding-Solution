#User function Template for python3

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        temp = []
        for i in range(len(v)):
            if v[i] == x:
                temp.append(i)
                break
        for i in range(len(v)-1,-1,-1):
            if v[i] == x:
                temp.append(i)
                break
        if len(temp) == 0:
            return [-1,-1]
        return temp
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        ans = obj.indexes(a, k)
        if ans[0]==-1 and ans[1]==-1:
            print(-1)
        else:
            print(ans[0], end=' ')
            print(ans[1])

        T -= 1


        print("~")
if __name__ == "__main__":
    main()


# } Driver Code Ends