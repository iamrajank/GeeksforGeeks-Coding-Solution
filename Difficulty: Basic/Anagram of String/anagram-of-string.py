# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    
    #add code here
    lst1 = list(str1)
    lst2 = list(str2)
    lst3 = lst1 + lst2
    for i in lst3:
        if i in lst1 and i in lst2:
            lst1.remove(i)
            lst2.remove(i)
    return (len(lst1) + len(lst2))
    
    
    # temp1 = []
    # temp2 = []
    # for i in range(len(S1)):
    #     if S1[i] not in S1:
    #         temp1.append(S1[i])
            
    # for i in range(len(S2)):
    #     if S2[i] not in S1:
    #         temp2.append(S2[i])
            
    # result = temp1.extend(temp2)
    
    # result1 = set(result)
    
    # if len(result1) == 0:
    #     return -1
    
    # return len(result1)
    
    
            
            
    
    





#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(remAnagram(str1, str2))
        print("~")

# } Driver Code Ends