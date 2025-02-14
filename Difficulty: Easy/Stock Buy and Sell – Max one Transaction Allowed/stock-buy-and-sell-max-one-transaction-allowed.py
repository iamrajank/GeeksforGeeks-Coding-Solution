class Solution:
    def maximumProfit(self, prices):
        # code here
        buy_price = prices[0]
        m_profit = 0
        for i in range(1,len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                profit = prices[i] - buy_price
                m_profit = max(m_profit,profit)
        return m_profit


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends