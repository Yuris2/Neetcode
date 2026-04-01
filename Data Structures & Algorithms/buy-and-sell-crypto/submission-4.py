class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = 0
        sell = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            maxProfit = max(maxProfit, profit)

            if profit < 0:
                buy = sell
            
            sell += 1
        
        return maxProfit
        