#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        len_n = len(str(n))
        arm_num = 0
        n_copy = n
        while n > 0:
            digit = n % 10
            arm_num = arm_num + digit ** len_n
            n = n // 10
        if n_copy == arm_num:
            return True
        return False
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends