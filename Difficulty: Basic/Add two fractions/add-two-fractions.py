#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
    #Code here
    def lcm(a,b):
        while a!=0:
            a,b=b%a,a
        return b
    if den1==den2:
        newnum=num1+num2
        print(newnum,end='/')
        print(den1)
    else:
        numx=num1*den2+num2*den1
        denx=den1*den2
        g=lcm(numx,denx)
        print(numx//g,end='/')
        print(denx//g)
    
 
    








#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])

        print("~")
# } Driver Code Ends