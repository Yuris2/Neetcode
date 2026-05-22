class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n + 2)]

        for i in range(len(prices) - 1, -1, -1):
            for buy in range(1,-1,-1):
                dp[i][buy] = max(dp[i + 1][buy], dp[i + 1][1] - prices[i])
                if buy == 1:
                    dp[i][buy] = max(dp[i][buy], dp[i + 2][0] + prices[i])
        
        return dp[0][0]