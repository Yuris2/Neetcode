class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Pattern:
            #2D-DP where your choice has an effect on future decisions
        #General Idea
            #Buy a coin, == 0
                # -prices[i] + dp(i + 1)
            #Sell a coin == 1
                # +prices[i] + dp(i + 2)
        
        dp = [[0,0] for _ in range(len(prices) + 2)]


        for i in range(len(prices) - 1, -1, -1):
            for sell in range(1, -1, -1):
                dp[i][sell] = max(dp[i + 1][sell], dp[i + 1][1] - prices[i])
                if sell == 1:
                    dp[i][sell] = max(dp[i][sell], dp[i + 2][0] + prices[i])


        
        return dp[0][0]


        