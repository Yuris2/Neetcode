class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Depends on sell and next row
        dp = [[0,0] for _ in range(len(prices) + 2)]

        #Sell = True/1 | Buy = False/0
        for i in range(len(prices) - 1, -1, -1):
            for sell in range(1,-1,-1):
                if sell == 1:
                    cooldown = dp[i + 2][0]
                    dp[i][sell] = max(dp[i + 1][1], cooldown + prices[i])
                else:
                    c1 = dp[i + 1][1] - prices[i]
                    c2 = dp[i + 1][0]
                    dp[i][sell] = max(c1, c2)
        
        return dp[0][0]