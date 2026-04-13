class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for sell in range(1, -1, -1):
                #Sell
                if sell == 1:
                    cooldown = dp[i + 2][0] if i + 2 <= n else 0
                    #Sell at different point, compare to cooldown
                    dp[i][sell] = max(dp[i + 1][1], cooldown + prices[i]) 
                #Buy
                else:
                    #Buy a coin or skip the buy
                    dp[i][sell] = max(dp[i + 1][1] - prices[i], dp[i + 1][0])
        
        return dp[0][0]

        