#User function Template for python3

class Solution:
    def print_divisors(self, N):
        # code here
        
        # Naive solution
        
        # for i in range(1,N+1):
        #     if N % i == 0:
        #          print(i,end=" ")
        
        # optimal solution
        
        temp = []
        for i in range(1,int(N**0.5)+1):
            if N % i == 0:
                a = int(N / i)
                if i == a:
                    temp.append(i)
                else:
                    temp.append(i)
                    temp.append(a)
        for i in range(len(temp)):
            print(sorted(temp)[i],end=" ")
                
  
        
        
        
        
        

