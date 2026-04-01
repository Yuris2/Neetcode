class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]

            maxProfit = max(maxProfit, profit)

            if profit < 0:
                buy = sell
        
        return maxProfit

        