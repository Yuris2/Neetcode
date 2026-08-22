class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #After you sell a coin, you cannt buy another on the next day
        #You can only own one coint at a time (i.e buy once can't sell)

        dp = [[0,0] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            for sell in range(1, -1, -1):
                dp[i][sell] = max(dp[i][1] - prices[i], dp[i + 1][sell])
                if sell == 1:
                    dp[i][sell] = max(dp[i + 2][0] + prices[i], dp[i][sell])
        
        return dp[0][0]
                                    

