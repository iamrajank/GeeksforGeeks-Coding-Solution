#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        #code here 
    #     if n == 0:
    #         return 1
    #     else:
    #         return n * self.factorialNumbers(n-1)
    
    # Brute force
    
        # temp = []
        # fact = 1
        # for i in range(1,n+1):
        #     for j in range(1,i+1):
        #         fact = fact * j
        #     if fact <= n:
        #         temp.append(fact)
        #         fact= 1
        # return temp
        
        # temp = []
    # 	fact = 1
    # 	for i in range(1,n+1):
    # 	    fact = fact * i
    # 	    temp.append(fact)
    	
    # 	result = []  
    # 	for i in temp:
    # 	    if i < n+1:
    # 	        result.append(i)
    # 	return result
        
        
        temp = []
        fact = 1
        i = 1
    
        while fact <= n:
            temp.append(fact)
            i += 1
            fact *= i
    
        return temp
            


